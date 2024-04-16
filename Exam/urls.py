"""
URL configuration for Exam project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls,name='Admin2'),
    path('Admin',views.Admin,name='Admin'),
    path('',views.main,name='main'),
    path('Support',views.Support,name='Support'),
    path('Support2',views.Support2,name='Support2'),
    path('Contact',views.Contact,name='Contact'),
    path('About',views.AboutUs,name='AboutUs'),
    path('Settings',views.Settings,name='Settings'),
    path('Success/', views.success, name='Success'),    
    path('deleteBooking/<name>/', views.deleteBooking, name='deleteBooking'),
    path('editBooking/<name>/', views.editBooking, name='editBooking'),
    path('viewBookings/', views.a_viewBookings, name='viewBooking'), 
    path('Register', views.register, name='register'), 
        
]
