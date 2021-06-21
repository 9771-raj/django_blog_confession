
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your models here.
class contact(models.Model):
      name=models.CharField(max_length=30)
      email=models.EmailField()
      comments=models.TextField(max_length=500)

class confession(models.Model):
      date_posted=models.DateField(default=timezone.now)
      writter=models.ForeignKey(User,on_delete=models.CASCADE)
      title=models.CharField(max_length=30)
      conf_img=models.ImageField(upload_to='pictures')
      content=models.TextField(max_length=1000)

class blog(models.Model):
      author=models.ForeignKey(User,on_delete=models.CASCADE)
      date_blog=models.DateField(default=timezone.now)
      title=models.CharField(max_length=30)
      blog_img=models.ImageField(upload_to='pictures')
      content=models.TextField(max_length=1000)




      