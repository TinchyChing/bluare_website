from django.db import models

class Users(models.Model):
    email = models.EmailField(max_length=100)
    head = models.ImageField(upload_to = './static/upload/head',default='./static/images/user.jpg')
    password = models.TextField(max_length=64)
    username = models.TextField(max_length=100)
    age = models.IntegerField(default=0)
    birthday = models.TextField(max_length=100)
    phone = models.TextField(max_length=100)
    country = models.TextField(max_length=100)
    register_date = models.DateTimeField(auto_now_add=True, editable = True)

    def __str__(self):
        return self.email