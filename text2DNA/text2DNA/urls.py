"""untitled2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.conf import settings

from text2DNA_app import views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^', views.main_page, name='text2DNA'),
    url(r'^home4txt/', views.text_to_DNA, name='home4txt'),
    url(r'^home4DNA/', views.DNA_to_text, name='home4DNA'),
]
