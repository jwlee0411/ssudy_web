# Generated by Django 4.0 on 2023-06-05 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0008_clubs_file5_1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maintenance', models.TextField(max_length=10)),
                ('text', models.TextField(max_length=200)),
            ],
        ),
    ]
