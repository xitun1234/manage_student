from django.db import models
from giaovien.models import Teacher
from lophoc.models import LopHoc
from monhoc.models import MonHoc

# Create your models here.
class GiangDay(models.Model):
    maKeHoachGiangDay = models.AutoField(primary_key=True)
    maLopHoc = models.ForeignKey(LopHoc, on_delete=models.CASCADE)
    maMonHoc = models.ForeignKey(MonHoc, on_delete=models.CASCADE)
    maGiaoVienDay = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    hocKy = models.IntegerField()
    namHoc = models.IntegerField()
    