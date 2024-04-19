from rest_framework.generics import CreateAPIView

from apps.categories.models import Category
from apps.categories.serializers import CategorySerializer

class CategoryViewSet(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
