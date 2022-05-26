from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Teacher(AbstractUser):
    maGiaoVien = models.AutoField(primary_key=True)
    phoneNumber = models.CharField(default='',max_length=15)
    diaChi = models.CharField(default='',max_length=255)
    isGVCN = models.BooleanField(default=False)
    

