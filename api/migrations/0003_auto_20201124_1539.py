# Generated by Django 3.1.3 on 2020-11-24 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201124_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apisearchcall',
            name='query',
            field=models.CharField(max_length=255),
        ),
    ]
