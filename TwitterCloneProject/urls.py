"""TwitterCloneProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from MHB.views import register,user_login,user_logout,profile,profile_setting,follow,unfollow,feed

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_login , register, admin.site.urls),
    path('login/', admin.site.urls),
    path('logout/', user_logout, name='user_logout'),
    path('<str:username>/',profile, name='profile'),
    path('<str:username>/setting', profile_setting, name='profile_setting'),
    path('follow/<str:username>',follow, name='follow'),# return to father page
    path('unfollow/<str:username>',unfollow, name='unfollow'),  # return to father page
    path ('feed/',feed,name='feed'),
    path('admin/', admin.site.urls),
]
