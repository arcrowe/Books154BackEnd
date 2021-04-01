from rest_framework import routers
from .viewsets import UserViewSet, CustomerViewSet

app_name = 'users'

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('customers', CustomerViewSet)
