from django.urls import path
from apps.categories.views import CategoryViewSet 


urlpatterns = [
    path('api/categories/', CategoryViewSet.as_view(), name='api/categories/')
]