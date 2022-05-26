from dataclasses import fields
from django import forms 
from django.contrib.auth import get_user_model
from .models import Teacher
from lophoc.models import LopHoc
from monhoc.models import MonHoc

User = get_user_model()

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','diaChi','phoneNumber')
        

class ThemGiaoVienForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('username','password','email','first_name','last_name','phoneNumber','isGVCN')



    

class AddStudentForm(forms.Form):
    
    hoTen=forms.CharField(label="Họ Tên",max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    phoneNumber=forms.CharField(label="Số Điện Thoại",max_length=15,widget=forms.TextInput(attrs={"class":"form-control"}))
    email=forms.CharField(label="Địa Chỉ Email",max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    dob=forms.DateField(label="Ngày Tháng Năm Sinh")
    address=forms.CharField(label="Địa Chỉ Nhà",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    
    gender_choice=(
        ("Male","Nam"),
        ("Female","Nữ")
    )

    sex=forms.ChoiceField(label="Giới Tính",choices=gender_choice,widget=forms.Select(attrs={"class":"form-control"}))
    
class EditStudentForm(forms.Form):
    hoTen=forms.CharField(label="hoTen",max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    phoneNumber=forms.CharField(label="phoneNumber",max_length=15,widget=forms.TextInput(attrs={"class":"form-control"}))
    email=forms.CharField(label="email",max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    dob=forms.DateField()
    address=forms.CharField(label="Address",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    
    gender_choice=(
        ("Male","Nam"),
        ("Female","Nữ")
    )

    sex=forms.ChoiceField(label="Sex",choices=gender_choice,widget=forms.Select(attrs={"class":"form-control"}))


class AddGradeForm(forms.Form):
    
    tenLopHoc=forms.CharField(label="Tên Lớp Học",max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    moTa=forms.CharField(label="Mô Tả",max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    siSoLop=forms.IntegerField(label="Sỉ Số Lớp",widget=forms.TextInput(attrs={"class":"form-control"}))
    namHoc=forms.IntegerField(label="Năm Học",widget=forms.TextInput(attrs={"class":"form-control"}))
    
    
    maGVCN_List = []
    try:
        teachers = Teacher.objects.all()
        print("tét")
        
        for teacher in teachers:
            username_last_name = teacher.last_name + " | " + teacher.username
            small_info_teacher=(teacher.maGiaoVien,username_last_name)
            maGVCN_List.append(small_info_teacher)
    except:
        maGVCN_List=[]
    
    print(maGVCN_List)
   
    maGVCN = forms.ChoiceField(label="Giáo viên đảm nhận chủ nhiệm lớp",choices=maGVCN_List,widget=forms.Select(attrs={"class":"form-control"}))
    
class EditGradeForm(forms.Form):
    tenLopHoc=forms.CharField(label="Tên Lớp Học",max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    moTa=forms.CharField(label="Mô Tả",max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    siSoLop=forms.IntegerField(label="Sỉ Số Lớp",widget=forms.TextInput(attrs={"class":"form-control"}))
    namHoc=forms.IntegerField(label="Năm Học",widget=forms.TextInput(attrs={"class":"form-control"}))
    
    
    maGVCN_List = []
    try:
        teachers = Teacher.objects.all()
        print("tét")
        
        for teacher in teachers:
            username_last_name = teacher.last_name + " | " + teacher.username
            small_info_teacher=(teacher.maGiaoVien,username_last_name)
            maGVCN_List.append(small_info_teacher)
    except:
        maGVCN_List=[]
   
    maGVCN = forms.ChoiceField(label="Giáo viên đảm nhận chủ nhiệm lớp",choices=maGVCN_List,widget=forms.Select(attrs={"class":"form-control"}))
    
    
class AddTeacherForm(forms.Form):
    
    first_name=forms.CharField(label="Họ",max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name=forms.CharField(label="Tên",max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    email=forms.CharField(label="Email",max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    phoneNumber=forms.CharField(label="Số Điện Thoại",max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    isGVCN=forms.BooleanField(label="Là Giáo Viên Chủ Nhiệm",widget=forms.TextInput(attrs={"class":"form-control"}))
       
  
class EditTeacherForm(forms.Form):
    first_name=forms.CharField(label="Họ",max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name=forms.CharField(label="Tên",max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    email=forms.CharField(label="Email",max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    phoneNumber=forms.CharField(label="Số Điện Thoại",max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))

    gvcn_choice=(
        ("True","Chọn"),
        ("false","Không")
    )

    isGVCN=forms.ChoiceField(label="Là Giáo Viên Chủ Nhiệm",choices=gvcn_choice,widget=forms.Select(attrs={"class":"form-control"}))


class AddCourseForm(forms.Form):
    
    tenMonHoc=forms.CharField(label="Tên Môn Học",max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    moTa=forms.CharField(label="Mô Tả",max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    
    
    maLopHoc_List = []
    try:
        grades = LopHoc.objects.all()
        print("tét")
        
        for grade in grades:
            
            small_info_course=(grade.maLopHoc,grade.tenLopHoc)
            maLopHoc_List.append(small_info_course)
    except:
        maLopHoc_List=[]
   
    maLopHoc = forms.ChoiceField(label="Lớp Học",choices=maLopHoc_List,widget=forms.Select(attrs={"class":"form-control"}))
    

class EditCourseForm(forms.Form):
    
    tenMonHoc=forms.CharField(label="Tên Môn Học",max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    moTa=forms.CharField(label="Mô Tả",max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    
    
    maLopHoc_List = []
    try:
        grades = LopHoc.objects.all()
        print("tét")
        
        for grade in grades:
            
            small_info_course=(grade.maLopHoc,grade.tenLopHoc)
            maLopHoc_List.append(small_info_course)
    except:
        maLopHoc_List=[]
   
    maLopHoc = forms.ChoiceField(label="Lớp Học",choices=maLopHoc_List,widget=forms.Select(attrs={"class":"form-control"}))