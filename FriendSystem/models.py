from django.db import models
from django.utils import timezone


class Friends(models.Model):
    email = models.EmailField(max_length=100,default="x@xx.com")
    friends = models.TextField(default="[]")

    def __str__(self):
        return self.email
# Create your models here.

class AddMessage(models.Model):
    email = models.EmailField(max_length=100)
    message = models.TextField(default="[]")
    disagree = models.TextField(default="[]")
    def __str__(self):
        return  self.email

class MessageBox(models.Model):
    email = models.EmailField(max_length=100)
    email_to = models.EmailField(max_length=100)
    content = models.TextField(default="")
    date = models.DateTimeField('保存日期',default = timezone.now)
    def __str__(self):
        return self.email
