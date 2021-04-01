from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer, CustomerSerializer
from .permissions import IsUserOwnerOrGetAndPostOnly
from .models import Customer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsUserOwnerOrGetAndPostOnly, ]


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
