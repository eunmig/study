from django.urls import path, include
from . import views

urlpatterns = [
    path('get_data/<str:username>/', views.get_user_data),
    path('get_data/', views.get_user_datas),
    path('update_profile/<int:user_pk>/', views.update_profile),
    path('cars/', views.get_carinfo),
    path('my_cars/<int:salary_level>/', views.get_my_cars),
    path('car/<int:car_pk>', views.get_one_car),
]
