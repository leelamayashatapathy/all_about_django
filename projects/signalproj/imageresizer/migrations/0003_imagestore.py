# Generated by Django 5.0.6 on 2024-08-09 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageresizer', '0002_student_student_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('thumbnail_small', models.ImageField(blank=True, null=True, upload_to='images/thumbnails')),
                ('thumbnail_medium', models.ImageField(blank=True, null=True, upload_to='images/thumbnails')),
                ('thumbnail_large', models.ImageField(blank=True, null=True, upload_to='images/thumbnails')),
            ],
        ),
    ]
