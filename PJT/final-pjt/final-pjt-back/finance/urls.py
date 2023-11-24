from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),

    #적금
    path('save-deposit-products/', views.save_DP),
    path('deposit-products/', views.deposit_products),
    path('deposit-product/<str:fin_prdt_cd>/', views.get_deposit_item),
    path('deposit-products/top_rate/', views.top_rate_D),
    path('likes/<str:product_cd>/', views.likes_d),
    path('liked-products/', views.liked_D_products),
    path('deposit-product-options/<str:fin_prdt_cd>/', views.deposit_PO),

    #예금
    path('save-saving-products/', views.save_SP),
    path('saving-products/', views.saving_products),
    path('saving-product/<str:fin_prdt_cd>/', views.get_saving_item),
    path('saving-products/top_rate/', views.top_rate_S),
    path('saving-like/<str:product_cd>/', views.likes_s),
    path('liked-saving/', views.liked_S_products),
    path('saving-product-options/<str:fin_prdt_cd>/', views.deposit_SO),

]
