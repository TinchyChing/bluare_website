from django.db import models
import time
# Create your models here.

class PostContent(models.Model):
    email = models.EmailField(max_length=100)
    title = models.TextField(max_length=250,default="")
    content_type = models.CharField(max_length=5,default="动态")
    blog_type = models.CharField(max_length=5,default="游记")
    photo_type = models.CharField(max_length=5,default="游记")
    content = models.TextField(max_length=250)
    image = models.ImageField(upload_to = './static/upload/post/%s'%str(time.strftime( "%Y-%m-%d %X", time.localtime() )),default='./static/images/user.jpg')
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
