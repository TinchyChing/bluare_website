from django.db import models
import time

class Users(models.Model):
    email = models.EmailField(max_length=100)
    head = models.ImageField(upload_to = './static/upload/head',default='./static/images/user.jpg')
    sex = models.CharField(max_length=1,default="中性")
    password = models.TextField(max_length=64)
    username = models.TextField(max_length=100)
    age = models.IntegerField(default=0)
    birthday = models.TextField(max_length=100,default=time.strftime("%Y/%m/%d", time.localtime()))
    phone = models.TextField(max_length=100)
    country = models.TextField(max_length=100)
    is_online = models.BooleanField(max_length=1,default=False)
    register_date = models.DateTimeField(auto_now_add=True, editable = True)

    def __str__(self):
        return self.email



