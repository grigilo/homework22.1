# Generated by Django 5.0.4 on 2024-05-23 09:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_release'),
    ]

    operations = [
        migrations.AlterField(
            model_name='release',
            name='blog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='releases', to='blogs.blog', verbose_name='блог'),
        ),
    ]
