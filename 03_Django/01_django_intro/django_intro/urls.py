"""django_intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
"""
url 은 집배원과 같은 역할. 주소가 왔네? 어디로 보내야지? view로 가네? 보내줘야지
주소창으로 요청이 들어오면 그에맞는 view로 보내주는 역할.
"""
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('pull/', views.pull),
    path('push/', views.push),
    path('user_create/', views.user_create),
    path('user_new', views.user_new),
    path('result/', views.result),
    path('art/', views.art),
    path('pong/', views.pong),
    path('ping/', views.ping),
    path('catch/', views.catch),
    path('throw/', views.throw),
    path('lottos/', views.lottos),
    path('ispal/<character>', views.ispal),
    path('isbirth/', views.isbirth),
    path('template_language/', views.template_language),
    path('area/<int:r>', views.area),
    path('intro/<name>/<int:age>', views.intro),
    path('mux/<int:num1>/<int:num2>', views.mux),
    path('hello/<name>/<int:age>', views.hello),
    path('image/', views.image),
    path('dinner/', views.dinner),
    path('index/', views.index),
    path('introduce/', views.introduce),
    path('admin/', admin.site.urls),
]
