# Generated by Django 4.0 on 2023-05-06 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserve',
            name='room_number',
        ),
    ]
