from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    email = models.TextField(max_length=30)
    email2 = models.TextField(max_length=30)
    phone_number = models.TextField(max_length=30)
    dept = models.TextField(max_length=30)
    num = models.TextField(max_length=30)
    # account_type = models.TextField(max_length=30)
    # club_type = models.TextField(max_length=30, blank=True, null=True)
    # club_name = models.TextField(max_length=30, blank=True, null=True)
    first_name = models.TextField(max_length=30)

class ClubInfo(models.Model):
    #  fields = ('image', 'description', 'sns1_name', 'sns2_name', 'sns1_link', 'sns2_link')
    club_name = models.TextField(max_length=100, blank=True, null=True)
    club_category = models.TextField(max_length=100, blank=True, null=True)
    image = models.FileField(null=True, upload_to="", blank=True)
    description = models.TextField(max_length=100, blank=True, null=True)

    sns1_name = models.TextField(max_length=100, blank=True, null=True)
    sns2_name = models.TextField(max_length=100, blank=True, null=True)
    sns1_link = models.TextField(max_length=100, blank=True, null=True)
    sns2_link = models.TextField(max_length=100, blank=True, null=True)

    intro_01 = models.TextField(max_length=1000, blank=True, null=True)
    intro_02 = models.TextField(max_length=1000, blank=True, null=True)
    leader = models.TextField(max_length=200, blank=True, null=True)
    room = models.TextField(max_length=30, blank=True, null=True)
    year = models.TextField(max_length=30, blank=True, null=True)

    image_01 = models.FileField(null=True, upload_to="", blank=True)
    image_02 = models.FileField(null=True, upload_to="", blank=True)
    image_03 = models.FileField(null=True, upload_to="", blank=True)
    image_04 = models.FileField(null=True, upload_to="", blank=True)

class EmailVerify(models.Model):
    verify = models.TextField(max_length=10)