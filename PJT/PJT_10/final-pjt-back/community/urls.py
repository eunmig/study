from django.urls import path, include
from . import views

app_name='community'

urlpatterns = [
    path('category/', views.category_list),
    path('category_create/', views.category_create), #admin only
    path('posts/', views.post_list),
    path('post/<int:post_pk>/', views.post_detail),
    path('post_UD/<int:post_pk>/', views.post_UD),
    path('posts/<int:category_pk>/post/', views.post_create),
    path('comments/', views.comment_list),
    path('posts/<int:post_pk>/comment/', views.comment_create),
    path('comments/<int:comment_pk>/', views.comment_detail),
]
 