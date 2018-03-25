"""MyQuizProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.urls import include, path

from Home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
    # url(r'^$', views.home, name='home'),
    # path('', views.home, name = 'home'),
    # path(r'^home', views.home, name = 'home'),
    # path('home/', views.home, name = 'home'),
    # path('home/<int: year>', views.home, name = 'home'),
    # path(r'^home/<int: year>', views.home, name = 'home'),
    # url(r'^practise', views.practise, name = 'practise'),
    # url(r'^ccat_practise', views.ccat_practise, name = 'ccat_practise'),
    # url(r'^cdac_practise', views.cdac_practise, name = 'cdac_practise'),
    # url(r'^aptitude', views.aptitude, name = 'aptitude'),
]
