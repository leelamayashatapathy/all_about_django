# Generated by Django 5.0.6 on 2024-08-05 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0018_student2_age_gte_18'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='person',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
    ]
