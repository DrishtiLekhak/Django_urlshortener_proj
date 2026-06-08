from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def registerPage(request):

    if request.method == 'POST':
        data = request.POST
        fname = data['firstName']
        lname = data['lastName']
        em = data['email']
        uname = data['username']
        psw = data['password']
        cpsw = data['confirmpassword']

        if User.objects.filter(username=uname).exists():
            messages.error(request,'User with this username already exist!!!')
            return redirect('register_page')

        if psw != cpsw:
            messages.error(request,'Password doesnt match!!!!')
            return redirect('register_page')
        
        User.objects.create_user(first_name=fname,last_name=lname,username=uname,email=em,password=psw)
        messages.success(request,'Register Successfully!!!')
        return redirect('register_page')


    return render(request,'Register.html')

def loginPage(request):

    if request.method == 'POST':
        data = request.POST
        uname = data['username']
        psw = data['password']

        user = authenticate(request, username=uname, password = psw)

        if user is not None:
            login(request,user)
            messages.success(request,'Login Succesfully!!!')
            return redirect('dashboard_page')     

        else:
            messages.error(request,'Username or Password doesnot match!!!')
            return redirect('login_page')


    return render(request,'Login.html')

def logoutPage(request):
    logout(request)
    return redirect('index_page')