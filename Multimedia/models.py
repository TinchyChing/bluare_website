from django.db import models
from django.utils import timezone
# 视频结构模型

# 用户视频
class UsersVideo(models.Model):
    email = models.EmailField(max_length = 100)
    title = models.TextField(max_length=100,default="video")
    videos = models.TextField(max_length=200)
    type = models.CharField(max_length=20,default="video")
    date = models.DateTimeField('保存日期',default = timezone.now)
    def __str__(self):
        return self.email
