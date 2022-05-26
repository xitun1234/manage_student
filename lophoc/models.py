from django.db import models
from giaovien.models import Teacher
from hocsinh.models import HocSinh

# Create your models here.
class LopHoc(models.Model):
    maLopHoc = models.AutoField(primary_key=True)
    maGVCN = models.ForeignKey(Teacher, on_delete=models.CASCADE,)
    tenLopHoc = models.CharField(default='', max_length=100)
    
    moTa = models.CharField(default='', max_length=255)
    siSoLop = models.IntegerField()
    namHoc = models.IntegerField()
    
class LopHoc_HocSinh(models.Model):
    maLopHoc = models.ForeignKey(LopHoc,on_delete=models.CASCADE)
    maHocSinh = models.ForeignKey(HocSinh,on_delete=models.CASCADE)