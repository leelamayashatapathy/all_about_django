# Generated by Django 5.0.6 on 2024-08-06 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textsearch', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='tags',
        ),
    ]
