from django.urls import path
from .views import indexPage,dashboardPage,create_url,redirect_url,deleteUrl,editUrl

urlpatterns = [

    path('',indexPage,name='index_page'),
    path('dashboard/',dashboardPage,name='dashboard_page'),
    path('createurl/',create_url,name='create_url'),
    path('<str:code>/',redirect_url,name='redirect_url'),
    path('delete/<int:sid>',deleteUrl,name='delete_url'),
    path('edit/<int:sid>',editUrl,name='edit_url')

  
]
