"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from basic.views import home
from basic.views import add
from basic.views import health
from basic.views import cal
from basic.views import info
from basic.views import eww
from basic.views import hh
from basic.views import name
from basic.views import names
urlpatterns = [
    path('admin/', admin.site.urls),
    path('first/',home),
    path('second/',add),
    path('third/',health),
    path("4/",cal),
    path("siva/",info),
    path("subba/",eww),
    path("ravi/",hh),
    path("hi/",name),
    path("danjo/",names)
]
