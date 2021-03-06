# Generated by Django 3.1.5 on 2021-02-21 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.CharField(blank=True, max_length=280, null=True),
        ),
        migrations.CreateModel(
            name='Special',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default=None, max_length=25)),
                ('books', models.ManyToManyField(related_name='categories', to='books.Book')),
            ],
        ),
    ]
