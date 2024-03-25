from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.home, name='home'),
    path('login/',views.login_page, name='login'),
    path('logout/',views.logout_admin, name='logout'),
    # path('register/',views.register_page, name='register'),
    
    path('singular/', views.singular, name='singular'),
    path('multiple/', views.multiple, name='multiple'),
    
    path('import/',views.importExcel, name='push_excel'),

    # path('customer/', views.customer, name='customer'),
    # path('add_customer/', views.add_customer, name='add_customer'),
    # path('edit_customer/<str:pk>/', views.edit_customer, name='edit_customer'),
    # path('delete_customer/<str:pk>/', views.delete_customer, name= 'delete_customer'),
    # path('customer_details/<str:pk>',views.customer_details, name='customer_details'),
    
]