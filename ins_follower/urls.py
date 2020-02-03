"""ins_follower URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from follower.views import views
from follower.views.sign_in import sign_in

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('recommend/', views.home_recommend),
    path('myfocus/', views.home_focus_list),
    path('index/', views.index),
    path('explore/', views.explore_images),
    path('register/', sign_in.register),
    path('login/', views.login),
    path('account/', views.account),
    path('tk/', sign_in.get_tk),
    path('auth/<i>/', sign_in.auth_email_or_phone)
]
