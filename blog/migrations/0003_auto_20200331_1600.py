# Generated by Django 3.0.4 on 2020-03-31 13:00

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='article'),
        ),
        migrations.AlterField(
            model_name='author',
            name='avator',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='avator'),
        ),
    ]
