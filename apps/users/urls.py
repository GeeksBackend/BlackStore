from django.urls import path

from apps.users.views import UserAPI, UserAPIDetail

urlpatterns = [
    path('api/users/', UserAPI.as_view(), name="api_users"),
    path('api/users/<int:pk>/', UserAPIDetail.as_view(), name="api_users_detail")
]