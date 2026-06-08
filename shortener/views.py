from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
import random
import string
from .models import ShortURL
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

# Create your views here.
def indexPage(request):
    return render(request,'main/home.html')

@login_required(login_url='login_page')
def dashboardPage(request):
    urls=ShortURL.objects.filter(user=request.user)
    return render(request,'main/dashboard.html',{'urls':urls})

def generate_code():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=6))

def create_url(request):

    if request.method == 'POST':
        data = request.POST

        original_url = data['original_url']

        short_code = generate_code()
        while ShortURL.objects.filter(short_code=short_code).exists():
            short_code = generate_code()

        ShortURL.objects.create(user=request.user,original_url=original_url,short_code=short_code)
        return redirect('dashboard_page')

        
    return render(request,'main/CreateUrl.html')

def redirect_url(request,code):
    url = get_object_or_404(ShortURL, short_code=code)

    #click count logic
    url.click_count += 1
    url.save()

    #redirect to original URL
    return redirect(url.original_url)

def deleteUrl(request,sid):
    ShortURL.objects.filter(id=sid).delete()
    messages.success(request,'Url deleted succesfully!!!')
    return redirect('dashboard_page')

def editUrl(request,sid):

    url=ShortURL.objects.get(id=sid)

    if request.method == 'POST':
        data = request.POST
        new_url = data['original_url']


        url.original_url = new_url
        url.save()
        messages.success(request,'Url edited successfully!!')
        return redirect('dashboard_page')

    return render(request,'main/EditUrl.html',{'url':url})
