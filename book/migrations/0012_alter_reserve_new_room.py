# Generated by Django 4.0 on 2023-12-22 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0011_reserve_new_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserve_new',
            name='room',
            field=models.CharField(max_length=100),
        ),
    ]
