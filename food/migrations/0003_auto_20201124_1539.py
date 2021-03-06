# Generated by Django 3.1.3 on 2020-11-24 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_auto_20201123_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodproduct',
            name='product_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='ingredient_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='nutrient',
            name='nutrient_name',
            field=models.CharField(max_length=255),
        ),
    ]
