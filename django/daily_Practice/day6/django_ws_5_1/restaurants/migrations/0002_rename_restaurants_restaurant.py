# Generated by Django 4.2.2 on 2023-09-26 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Restaurants',
            new_name='Restaurant',
        ),
    ]