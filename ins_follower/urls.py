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
from django.conf.urls import url
from django.views import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('recommend/', views.home_recommend),
    path('myfocus/', views.home_focus_list),
    path('index', views.index, kwargs={'x': 'y'}),
    path('explore/', views.explore_images),
    path('register/', sign_in.register, name='register'),
    path('login/', sign_in.my_login, name='login'),
    path('account/', views.account),
    path('tk/', sign_in.get_tk),
    path('auth/', sign_in.auth_email_or_phone),
    path('ts1/', views.test1),
    path('ts2', views.test2)
]
