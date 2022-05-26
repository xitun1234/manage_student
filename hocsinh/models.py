from django.db import models

# Create your models here.

class HocSinh(models.Model):
    maHocSinh = models.AutoField(primary_key=True)
    hoTen = models.CharField(default='',max_length=100)
    diaChi = models.CharField(default='',max_length=255)
    dob = models.DateField(null=True)
    phoneNumber = models.CharField(default='',max_length=15,null=True)
    email = models.CharField(default='',max_length=255,null=True)
    gioiTinh = models.CharField(max_length=255,null=True)
    status = models.BooleanField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.hoTen)
    
class XepLoai(models.Model):
    maXepLoai = models.AutoField(primary_key=True)
    maHocSinh = models.ForeignKey(HocSinh, on_delete=models.CASCADE)
    diemTongKet = models.IntegerField()
    hanhKiem = models.CharField(default='',max_length=50)
    xepLoai = models.CharField(default='',max_length=50)
    lopHoc = models.IntegerField()