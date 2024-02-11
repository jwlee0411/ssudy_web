import datetime

from django.db import models
from django.utils.crypto import get_random_string
from django.utils.html import mark_safe
import markdown

class Search(models.Model):
    search = models.TextField(max_length=100)

class Board(models.Model):
    board_title = models.TextField(max_length=100, unique=True)
    sub_id = models.IntegerField(unique=True)
    is_superuser = models.BooleanField()
    board_seq = models.IntegerField()


class Post(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField(max_length=5050)
    def get_markdown_content(self):
        return mark_safe(markdown.markdown(self.content))

    create_date = models.DateTimeField(auto_now_add=True)

    name = models.TextField(max_length=100)

    board = models.CharField(max_length=100)

    file1 = models.FileField(null=True, upload_to="", blank=True)

    file2 = models.FileField(null=True, upload_to="", blank=True)

    file3 = models.FileField(null=True, upload_to="", blank=True)

    file4 = models.FileField(null=True, upload_to="", blank=True)

    file5 = models.FileField(null=True, upload_to="", blank=True)

    file_reset = models.BooleanField(default=False)
