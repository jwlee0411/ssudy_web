from django.db import models

class Email(models.Model):
    email1 = models.TextField(null=False, blank=False)

class EmailAll(models.Model):
        email1 = models.TextField(null=False, blank=False)
        email2 = models.TextField(null=False, blank=False)
class Popup(models.Model):
    file1 = models.FileField(null=True, upload_to="", blank=True)
    content1 = models.TextField(null=True, blank=True)

class AddClass(models.Model):
    name = models.TextField(max_length=100)
    confirm = models.BooleanField(default=False)

class Maintenance(models.Model):
    text = models.TextField(max_length=200)

class Terms(models.Model):
    file1 = models.FileField(null=True, upload_to="", blank=True)
    file2 = models.FileField(null=True, upload_to="", blank=True)
    file3 = models.FileField(null=True, upload_to="", blank=True)

class ClassSetting(models.Model):
    club_start = models.TextField(max_length=100)
    club_end = models.TextField(max_length=100)
    stu_start = models.TextField(max_length=100)
    stu_end = models.TextField(max_length=100)


class Clubs(models.Model):
    file1_1 = models.FileField(null=True, upload_to="", blank=True)
    file1_2 = models.FileField(null=True, upload_to="", blank=True)
    file1_3 = models.FileField(null=True, upload_to="", blank=True)
    file2_1 = models.FileField(null=True, upload_to="", blank=True)
    file2_2 = models.FileField(null=True, upload_to="", blank=True)
    file2_3 = models.FileField(null=True, upload_to="", blank=True)
    file3_1 = models.FileField(null=True, upload_to="", blank=True)
    file3_2 = models.FileField(null=True, upload_to="", blank=True)
    file3_3 = models.FileField(null=True, upload_to="", blank=True)
    file4_1 = models.FileField(null=True, upload_to="", blank=True)
    file5_1 = models.FileField(null=True, upload_to="", blank=True)
    calendar_check = models.BooleanField(default=False)


class Front(models.Model):
    file1 = models.FileField(null=True, upload_to="", blank=True)
    file2 = models.FileField(null=True, upload_to="", blank=True)
    file3 = models.FileField(null=True, upload_to="", blank=True)

    title1 = models.TextField(null=True, blank=True)
    title2 = models.TextField(null=True, blank=True)
    title3 = models.TextField(null=True, blank=True)

    content1 = models.TextField(null=True, blank=True)
    content2 = models.TextField(null=True, blank=True)
    content3 = models.TextField(null=True, blank=True)


# class Board(models.Model):
#     group = models.TextField(null=True, blank=True)
#     title0 = models.TextField(null=True, blank=True)
#     permission = models.BooleanField()


class MainBoard(models.Model):
    board1 = models.TextField(null=True, blank=True)
    board2 = models.TextField(null=True, blank=True)
