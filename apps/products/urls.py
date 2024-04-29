from django.urls import path
from apps.products.views import ProductViewSet, ProductDetailAPI


urlpatterns = [
    path('products/', ProductViewSet.as_view(), name='api/products/'),
    path('products/<int:pk>/', ProductDetailAPI.as_view(), name="api_product_detail")
]
