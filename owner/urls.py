from django.urls import path 

from . import views

app_name='onr'

urlpatterns=[ 
    path('login',views.login,name='login'),
    path('home',views.home,name='home')
]