from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('save-deposit-products/', views.save_DP),
    path('deposit-products/', views.deposit_products),
    path('deposit-product/<str:fin_prdt_cd>/', views.get_deposit_item),
    path('deposit-product-options/<str:fin_prdt_cd>/', views.deposit_PO),
    path('deposit-products/top_rate/', views.top_rate),
    path('likes/<str:product_cd>/', views.likes),
    path('liked_products/', views.liked_products),
]
