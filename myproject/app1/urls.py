from django.contrib import admin
from django.urls import path
from.import views 
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.index,name='index'),
    path('login/', views.user_login, name='user_login'),
    path('register/', views.register, name ='register'),
    path('c1/', views.c1, name ='c1'),
    path('c2/', views.c2, name ='c2'),
    path('c3/', views.c3, name ='c3'),
    path('studenthome/', views.studenthome, name ='studenthome'),
    path('enroll/', views.enroll, name ='enroll'),
    path('task/', views.task, name ='task'),
    path('calendar/', views.calendar, name ='calendar'),
    path('dashboard/', views.dashboard, name ='dashboard'),
    path('admincourse/', views.admincourse, name ='admincourse'),
    path('studentlist/', views.studentlist, name ='studentlist'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('admincourse/', views.admincourse, name ='admincourse'),
    path('teacherhome/', views.teacherhome, name ='teacherhome'),
]


