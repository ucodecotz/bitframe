# Generated by Django 3.1.7 on 2021-04-13 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20210413_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='products',
            field=models.ManyToManyField(to='products.OrderedProducts'),
        ),
    ]
