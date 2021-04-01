from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20)
    authors = models.CharField(max_length=200)
    short_description = models.TextField()
    subtitle = models.TextField()
    long_description = models.TextField()
    publisher = models.CharField(max_length=50)
    publishedDate = models.DateField()
    category = models.CharField(max_length=50)
    cover = models.CharField(max_length=280, null=True, blank=True)
    format = models.CharField(max_length=20, default='Hard Cover')
    inStockNumber = models.IntegerField(default=10)
    language = models.CharField(max_length=10, default='en')
    numberSold = models.IntegerField(default=0)
    pageCount = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f'{self.title} - {self.authors} - {self.isbn}'


class Special(models.Model):
    display = models.BooleanField(default=False)
    logo = models.CharField(max_length=25, default='')
    type = models.CharField(max_length=25, default=None)
    books = models.ManyToManyField('Book', related_name='specials', blank=True)

    def __str__(self):
        return f'{self.type}'
