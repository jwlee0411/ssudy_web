# Generated by Django 4.0 on 2023-12-29 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0012_alter_reserve_new_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserve_new',
            name='confirm',
            field=models.BooleanField(default=False),
        ),
    ]