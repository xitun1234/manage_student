from django.db import models
from hocsinh.models import HocSinh
from monhoc.models import MonHoc
# Create your models here.
class LoaiKiemTra(models.Model):
    maLoaiBaiKiemTra = models.AutoField(primary_key=True)
    tenLoaiBaiKiemTra = models.CharField(default='',max_length=100)
    moTa = models.CharField(default='',max_length=100)
    
class Kiemtra(models.Model):
    maBaiKiemTra = models.AutoField(primary_key=True)
    maLoaiBaiKiemTra = models.ForeignKey(LoaiKiemTra, on_delete=models.CASCADE)
    tenBaiKiemTra = models.CharField(default='',max_length=50)
    ngayLamBaiKiemTra = models.DateField()
    
class KetQua_KiemTra(models.Model):
    maKetQua_KiemTra = models.AutoField(primary_key=True)
    maBaiKiemTra = models.ForeignKey(Kiemtra, on_delete=models.CASCADE)
    maHocSinh = models.ForeignKey(HocSinh,on_delete=models.CASCADE)
    maMonHoc = models.ForeignKey(MonHoc,on_delete=models.CASCADE)
    soDiem = models.IntegerField()