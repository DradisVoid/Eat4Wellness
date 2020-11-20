# Generated by Django 3.1.3 on 2020-11-16 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='admin status'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_coach',
            field=models.BooleanField(default=False, verbose_name='coach status'),
        ),
    ]