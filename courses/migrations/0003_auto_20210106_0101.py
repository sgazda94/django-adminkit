# Generated by Django 3.1.4 on 2021-01-06 00:01

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20201231_0323'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MyModel',
        ),
        migrations.AddField(
            model_name='module',
            name='content',
            field=tinymce.models.HTMLField(default=''),
        ),
    ]
