# Generated by Django 3.1.5 on 2021-02-21 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20210221_0814'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='format',
            field=models.CharField(default='Hard Cover', max_length=20),
        ),
        migrations.AddField(
            model_name='book',
            name='inStockNumber',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.CharField(default='en', max_length=10),
        ),
        migrations.AddField(
            model_name='book',
            name='numberPurchased',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='pageCount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
