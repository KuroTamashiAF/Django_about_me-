from . import views
from django.urls import path

urlpatterns = [
    path('main/', views.main, name='main'),
    path('about/', views.about_me, name='about_me'),
    path('dreams/', views.my_dreams, name='my_dreams'),
]
