from django.urls import path
from .views import registerPage,loginPage,logoutPage

urlpatterns = [

    path('register/',registerPage,name='register_page'),
    path('login/',loginPage,name='login_page'),
    path('logout/',logoutPage,name='logout_page')

]
