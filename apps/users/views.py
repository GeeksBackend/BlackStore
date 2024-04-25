from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.users.models import User
from apps.users.serializers import UserSerializer

# Create your views here.
class UserAPI(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserAPIDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer