# Generated by Django 3.2.15 on 2023-01-25 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Front',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file1', models.FileField(blank=True, null=True, upload_to='')),
                ('file2', models.FileField(blank=True, null=True, upload_to='')),
                ('file3', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
