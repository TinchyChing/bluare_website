from django.db import models

# Create your models here.

class PostContent(models.Model):
    email = models.EmailField(max_length=100)
    title = models.TextField(max_length=250,default="")
    content = models.TextField(max_length=250)
    comment = models.TextField
    date = models.TextField(max_length=100,default="2016-01-01 14:22:22")
    def __str__(self):
        return self.email

class Comment(models.Model):
    email = models.CharField
    comment_email = models.EmailField
    twice_comment = models.TextField(null=True)
    content = models.TextField(max_length=250)
    def __str__(self):
        return self.content

class T_Comment(models.Model):
    email = models.CharField
    # comment_email是表示评论者的邮箱
    comment_email = models.EmailField
    content = models.TextField(max_length=250)
    def __str__(self):
        return self.content
