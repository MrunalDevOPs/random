"""randomnumber URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from typing import ValuesView
from django.contrib import admin
from django.urls import path
from helloWorld import views

urlpatterns = [
    
    # path('',views.home),
    # path('about/', views.about),    
    # path('countries/',views.countries),
    # path('form/',views.form),
    # path('form/number',views.number,name='simple'),
    path('form1/',views.form1),
    path('form1/number',views.number,name='num'),
    path('form2/', views.form2, name= 'logout'),
    path('form2/home',views.home ,name='simple'),


    


]
