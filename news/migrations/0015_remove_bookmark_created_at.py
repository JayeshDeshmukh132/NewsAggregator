# Generated by Django 3.0.14 on 2024-04-09 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0014_bookmark_source'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmark',
            name='created_at',
        ),
    ]