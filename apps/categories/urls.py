from django.urls import path
from apps.categories.views import CategoryViewSet, CategoryDetailAPI


urlpatterns = [
    path('categories/', CategoryViewSet.as_view(), name='api/categories/'),
    path('categories/<int:pk>/', CategoryDetailAPI.as_view(), name="api_category_detail")
]