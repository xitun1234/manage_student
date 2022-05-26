from django.db import models
from giaovien.models import Teacher
from lophoc.models import LopHoc

# Create your models here.
class MonHoc(models.Model):
    maMonHoc = models.AutoField(primary_key=True)
    tenMonHoc = models.CharField(default='',max_length=50)
    moTa = models.CharField(default='',max_length=100)
    lopHoc = models.ForeignKey(LopHoc, on_delete= models.CASCADE)

    