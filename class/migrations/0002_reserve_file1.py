# Generated by Django 4.0 on 2023-12-12 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserve',
            name='file1',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
