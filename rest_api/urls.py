from django.urls import path
from rest_api import views

urlpatterns = [
    path('rest_api/', views.user_list),
    path('rest_api/<int:pk>/', views.user_detail),
]