from django.contrib import admin
from django.urls import path
from accountsapp import views



urlpatterns =[
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),


]