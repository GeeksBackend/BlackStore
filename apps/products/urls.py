from django.urls import path
from apps.products.views import ProductViewSet


urlpatterns = [
    path('api/products/', ProductViewSet.as_view(), name='api/products/')
]
