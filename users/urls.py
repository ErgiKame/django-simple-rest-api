from django.urls import path
from rest_api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('rest-api/get-users', views.user_list),
    path('rest-api/get-users/<int:pk>', views.user_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)