from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('save/', views.saveExchangeRate),
    path('get/', views.getExchangeRate)
]