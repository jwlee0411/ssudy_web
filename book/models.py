from django.db import models

class Reserve_new(models.Model):
    user_id = models.CharField(max_length=32)
    user_name = models.CharField(max_length=100)
    user_tel = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100)
    register_time = models.DateTimeField(auto_now_add=True)
    reserve_date = models.DateTimeField(default="2000-01-01")
    reserve_time = models.CharField(max_length=32)
    room = models.CharField(max_length=100)
    confirm = models.BooleanField(default=False)
    reserve_desc_1 = models.CharField(max_length=500, default="")
    reserve_desc_2 = models.CharField(max_length=500, default="")
    reserve_desc_3 = models.CharField(max_length=500, default="")
    reserve_num = models.CharField(max_length=50, default="")


