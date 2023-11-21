from django.urls import path, include
from . import views

urlpatterns = [
    path('get_data/<str:username>/', views.get_user_data),
    path('get_data/', views.get_user_datas),
    path('update_profile/<int:user_pk>/', views.update_profile)
    # path('profile_update/', views.profile_update)
]
