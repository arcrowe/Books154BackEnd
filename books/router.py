from rest_framework import routers
from .viewsets import BookViewSet, SpecialViewSet, BookSearchViewSet

app_name = 'books'

router = routers.DefaultRouter()
router.register('books', BookViewSet)
router.register('book', BookViewSet)
router.register('search', BookSearchViewSet)
router.register('specials', SpecialViewSet)
