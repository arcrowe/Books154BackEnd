from django.http import Http404
from rest_framework import viewsets, filters

# from .permissions import IsUserOwnerOrGetAndPostOnly
from .models import Book, Special
from .serializers import BookSerializer, SpecialSerializer


class BookSearchViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['title', 'authors']


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = super(BookViewSet, self).get_queryset()
        special_cat = self.request.query_params.get('special_category', None)
        single_book = self.request.query_params.get('id', None)

        if special_cat:
            try:
                # sp = Special.objects.get(type=special_name)
                sp = Special.objects.get(id=special_cat)
                queryset = queryset.filter(specials=sp.pk)
            except Special.DoesNotExist:
                raise Http404

            return queryset
        elif single_book:
            try:
                queryset = queryset.filter(id=single_book)
            except Special.DoesNotExist:
                raise Http404
            return queryset
        return queryset

        # permission_classes = [IsUserOwnerOrGetAndPostOnly, ]


class SpecialViewSet(viewsets.ModelViewSet):
    queryset = Special.objects.all().filter(display=True)
    serializer_class = SpecialSerializer
