# Generated by Django 3.1.3 on 2020-11-09 02:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0003_auto_20201108_2146'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodNutrient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('unit', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FoodProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Nutrient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nutrient_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MealFood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servings', models.PositiveIntegerField()),
                ('food_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.foodproduct')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.meal')),
            ],
        ),
        migrations.AddField(
            model_name='meal',
            name='food_products',
            field=models.ManyToManyField(through='food.MealFood', to='food.FoodProduct'),
        ),
        migrations.AddField(
            model_name='meal',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.member'),
        ),
        migrations.AddField(
            model_name='foodproduct',
            name='ingredients',
            field=models.ManyToManyField(to='food.Ingredient'),
        ),
        migrations.AddField(
            model_name='foodproduct',
            name='nutrients',
            field=models.ManyToManyField(through='food.FoodNutrient', to='food.Nutrient'),
        ),
        migrations.AddField(
            model_name='foodnutrient',
            name='food_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.foodproduct'),
        ),
        migrations.AddField(
            model_name='foodnutrient',
            name='nutrient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.nutrient'),
        ),
    ]
