# Generated by Django 3.2.18 on 2023-03-11 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='in_shopping_cart',
            new_name='is_in_shopping_cart',
        ),
    ]