# Generated by Django 5.0.6 on 2024-08-09 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageresizer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
