# Generated by Django 4.2.23 on 2025-07-04 12:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AllergyLabel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('starter', 'Starter'), ('main', 'Main'), ('sides', 'Sides'), ('salads', 'Salads'), ('drinks', 'Drinks'), ('desserts', 'Desserts'), ('chefs special', "Chef's Special")], default='starter', max_length=50)),
                ('description', models.TextField(default='')),
                ('price', models.FloatField(default=0.0)),
                ('allergy_labels', models.ManyToManyField(blank=True, related_name='menu_items', to='menu.allergylabel')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='menu.menu')),
            ],
            options={
                'ordering': ['category', 'title'],
            },
        ),
    ]
