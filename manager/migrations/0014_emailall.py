# Generated by Django 4.0 on 2023-12-22 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0013_rename_class_addclass'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailAll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email1', models.TextField()),
            ],
        ),
    ]
