# Generated by Django 4.2.2 on 2023-09-26 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_rename_restaurant_restaurent'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Restaurent',
            new_name='Restaurant',
        ),
    ]
