"""compartilhando URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from authuser.views import *
from authuser.forms import  UserCreationForm

urlpatterns = [
    url(r'^$', 'authuser.views.home', name='home'),
    url(r'^registrar/$', 'authuser.views.registrar', name='registrar'),
    url(r'^login/$', 'authuser.views.login_req', name='pagina_de_login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',{'next_page': 'home'}, name='logout'),
    url(r'cadastrar-anuncio/$', anuncioForm.as_view(), name='cria_anuncio'),
    url(r'^admin/', admin.site.urls),
]
