# Generated by Django 4.1.7 on 2023-02-27 01:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название ингридиента')),
                ('measurement_unit', models.CharField(choices=[('KG', 'кг'), ('GR', 'гр.')], max_length=200, verbose_name='единица измерения')),
            ],
            options={
                'verbose_name': 'ингридиент',
                'verbose_name_plural': 'ингридиенты',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Тег')),
                ('color', models.CharField(max_length=200, verbose_name='Цвет')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='media/', verbose_name='Картинка')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('text', models.TextField(help_text='Описание', verbose_name='Описание')),
                ('cooking_time', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Время приготовления (в минутах)')),
                ('ingredients', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='recipes.ingredients', verbose_name='ингридиент')),
                ('tags', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teg', to='recipes.tags', verbose_name='Тег')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
                'ordering': ('name',),
            },
        ),
    ]
