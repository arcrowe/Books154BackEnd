from rest_framework import serializers

from .models import Book, Special


class SpecialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Special
        fields = ['url', 'id', 'type', 'logo']


class BookSerializer(serializers.ModelSerializer):
    specials = SpecialSerializer(read_only=True, many=True)

    class Meta:
        model = Book
        fields = ('url', 'id', 'title', 'isbn', 'authors', 'short_description',
                  'subtitle', 'long_description', 'publisher', 'publishedDate',
                  'category', 'cover', 'format', 'inStockNumber', 'language',
                  'numberSold', 'pageCount', 'price', 'specials')
        extra_kwargs = {'specials': {'required': False}}
