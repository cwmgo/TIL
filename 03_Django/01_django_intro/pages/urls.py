from django.urls import path
from . import views

urlpatterns = [
    path('one/', views.one)
    path('static_example/', views.static_example),
    path('num/pull/', views.pull),
    path('num/push/', views.push),
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
]