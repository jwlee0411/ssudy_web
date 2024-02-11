from django.db import models

# Create your models here.

class Check(models.Model):
    checksum = models.TextField(max_length=100)



class Reserve(models.Model):
    name = models.TextField(max_length=100)
    club = models.TextField(max_length=100)
    phone_number = models.TextField(max_length=100)
    email = models.TextField(max_length=100)
    space = models.TextField(max_length=300)
    date = models.TextField(max_length=300)
    description = models.TextField(max_length=300)
    people = models.TextField(max_length=100)
    dy = models.TextField(max_length=100, default="")
    stu = models.TextField(max_length=100, default="")

    file1 = models.FileField(null=True, upload_to="", blank=True)

    checksum = models.TextField(max_length=10)
    create_date = models.DateTimeField(auto_now_add=True)