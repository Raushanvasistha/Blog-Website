from django.contrib import admin
from django.urls import path
from blogsapp import views



urlpatterns =[
    path('blog/', views.BlogsapiView, name='blog'),
    path('blog/<int:pk>/', views.BlogsapiView, name='details'),
    path('comment/', views.CommentsapiView, name='comment'),
    path('comment/<int:id>/', views.CommentsapiView),
]