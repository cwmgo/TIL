from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('mamago/', views.mamago), # (2)path를 보니 mamago가 있구나
    path('translated/', views.translated),
]