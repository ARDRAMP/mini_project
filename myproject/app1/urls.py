from django.contrib import admin
from django.urls import path
from.import views 


urlpatterns = [
    path('',views.index,name='index'),
    path('login/', views.user_login, name='user_login'),
    path('register/', views.register, name ='register'),
    path('c1/', views.c1, name ='c1'),
    path('c2/', views.c2, name ='c2'),
    path('c3/', views.c3, name ='c3'),
]
