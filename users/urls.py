from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.get_all_users),
    path('users/create/', views.create_user),
    path('users/<str:name>/', views.get_user_by_name),
]
