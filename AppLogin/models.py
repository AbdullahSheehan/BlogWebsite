from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_info')
    profilepic = models.ImageField(upload_to='profilePics/')
    