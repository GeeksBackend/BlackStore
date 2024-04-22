from rest_framework.generics import ListCreateAPIView

from apps.products.models import Product
from apps.products.serializers import ProductSerializer

class ProductViewSet(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
   