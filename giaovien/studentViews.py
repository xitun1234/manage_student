import json

import requests
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from giaovien.forms import AddStudentForm,EditStudentForm, AddGradeForm,EditGradeForm,EditTeacherForm,ThemGiaoVienForm,AddTeacherForm
from hocsinh.models import HocSinh
from lophoc.models import LopHoc
from giaovien.models import Teacher
from giaovien.forms import AddCourseForm,EditCourseForm
from monhoc.models import MonHoc

def add_student(request):
    form=AddStudentForm()
    return render(request,"themHocSinh.html",{"form":form})

def add_student_save(request):
    
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        form=AddStudentForm(request.POST,request.FILES)
        
        if form.is_valid():
            hoTen=form.cleaned_data["hoTen"]
            phoneNumber = form.cleaned_data["phoneNumber"]
            email = form.cleaned_data["email"]
            dob = form.cleaned_data["dob"]
            diaChi = form.cleaned_data["address"]
            gioiTinh = form.cleaned_data["sex"]
            status = True
          
            print(hoTen)
            try:
                newStudent =HocSinh(hoTen=hoTen,phoneNumber=phoneNumber,email=email,dob=dob,diaChi=diaChi,gioiTinh=gioiTinh,status=status)
                
                print(newStudent)
                newStudent.save()
                messages.success(request,"Thêm Học Sinh Mới Thành Công")
                return HttpResponseRedirect(reverse("add_student"))
            except:
                messages.error(request,"Lỗi Khi Thêm Học Sinh Mới")
                return HttpResponseRedirect(reverse("add_student"))
        else:
            form=AddStudentForm(request.POST)
            return render(request, "themHocSinh.html", {"form": form})
        

def manage_student(request):
    students=HocSinh.objects.all()

    return render(request,"quanLyHocSinh.html",{"students":students})

def edit_student(request,student_id):
    request.session['maHocSinh']=student_id
    student=HocSinh.objects.get(maHocSinh=student_id)
    form=EditStudentForm()
    form.fields['hoTen'].initial=student.hoTen
    form.fields['address'].initial=student.diaChi
    form.fields['dob'].initial=student.dob
    form.fields['phoneNumber'].initial=student.phoneNumber
    form.fields['email'].initial=student.email
    form.fields['sex'].initial=student.gioiTinh
   
    return render(request,"editHocSinh.html",{"form":form,"id":student_id,})


def edit_student_save(request):
    
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        maHocSinh=request.session.get("maHocSinh")
        
        form=AddStudentForm(request.POST,request.FILES)
        
        if form.is_valid():
            hoTen=form.cleaned_data["hoTen"]
            phoneNumber = form.cleaned_data["phoneNumber"]
            email = form.cleaned_data["email"]
            dob = form.cleaned_data["dob"]
            diaChi = form.cleaned_data["address"]
            gioiTinh = form.cleaned_data["sex"]
            
          
            try:
                student =HocSinh.objects.get(maHocSinh = maHocSinh)
                
                print(student)
                student.hoTen = hoTen
                student.phoneNumber = phoneNumber
                student.email = email
                student.dob = dob 
                student.diaChi = diaChi
                student.gioiTinh = gioiTinh
                student.save()
                messages.success(request,"Sửa thông tin học sinh thành công")
                return HttpResponseRedirect(reverse("edit_student",kwargs={"student_id":maHocSinh}))
            except:
                messages.error(request,"Lỗi Khi Sửa thông tin học sinh")
                return HttpResponseRedirect(reverse("edit_student",kwargs={"student_id":maHocSinh}))
        else:
            form=EditStudentForm(request.POST)
            student=HocSinh.objects.get(maHocSinh = maHocSinh)
            return render(request,"editHocSinh.html",{"form":form,"id":maHocSinh,})
        
        

def add_grade(request):
    form=AddGradeForm()
    return render(request,"themLopHoc.html",{"form":form})

def add_grade_save(request):
    
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        form=AddGradeForm(request.POST,request.FILES)
        
        if form.is_valid():
            tenLopHoc=form.cleaned_data["tenLopHoc"]
            moTa = form.cleaned_data["moTa"]
            siSoLop = form.cleaned_data["siSoLop"]
            namHoc = form.cleaned_data["namHoc"]
            maGVCN = form.cleaned_data["maGVCN"]
            
            print(tenLopHoc)
            print(moTa)
            print(siSoLop)
            print(namHoc)
            print(maGVCN)
            
            try:
                newGrade = LopHoc(maGVCN_id=maGVCN,tenLopHoc=tenLopHoc,moTa=moTa,siSoLop=siSoLop,namHoc=namHoc)
                print(newGrade)
                newGrade.save()
                messages.success(request,"Thêm Lớp Học Mới Thành Công")
                return HttpResponseRedirect(reverse("add_grade"))
            except:
                messages.error(request,"Lỗi Khi Thêm Lớp Học Mới")
                return HttpResponseRedirect(reverse("add_grade"))
        else:
            form=AddGradeForm(request.POST)
            return render(request, "themLopHoc.html", {"form": form})
        

def manage_grade(request):
    grades=LopHoc.objects.all()
    print(grades[0].maGVCN_id)
    
    return render(request,"quanLyLopHoc.html",{"grades":grades})

def edit_grade(request,maLopHoc):
    request.session['maLopHoc']=maLopHoc
    grade=LopHoc.objects.get(maLopHoc=maLopHoc)
    form=EditGradeForm()
    form.fields['tenLopHoc'].initial=grade.tenLopHoc
    form.fields['moTa'].initial=grade.moTa
    form.fields['siSoLop'].initial=grade.siSoLop
    form.fields['namHoc'].initial=grade.namHoc
    form.fields['maGVCN'].initial=grade.maGVCN

   
    return render(request,"editLopHoc.html",{"form":form,"id":maLopHoc,})

def edit_grade_save(request):
    
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        maLopHoc=request.session.get("maLopHoc")
        
        form=AddGradeForm(request.POST,request.FILES)
        
        if form.is_valid():
            tenLopHoc=form.cleaned_data["tenLopHoc"]
            moTa = form.cleaned_data["moTa"]
            siSoLop = form.cleaned_data["siSoLop"]
            namHoc = form.cleaned_data["namHoc"]
            maGVCN = form.cleaned_data["maGVCN"]
            
          
            try:
                grade =LopHoc.objects.get(maLopHoc = maLopHoc)
                
                print(grade)
                
                grade.tenLopHoc = tenLopHoc
                grade.moTa = moTa
                grade.siSoLop = siSoLop
                grade.namHoc = namHoc
                grade.maGVCN_id = maGVCN
                
                grade.save()
                messages.success(request,"Sửa thông tin lớp học thành công")
                return HttpResponseRedirect(reverse("edit_grade",kwargs={"maLopHoc":maLopHoc}))
            except:
                messages.error(request,"Lỗi Khi Sửa thông tin lớp học")
                return HttpResponseRedirect(reverse("edit_grade",kwargs={"maLopHoc":maLopHoc}))
        else:
            form=EditGradeForm(request.POST)
            grade=LopHoc.objects.get(maLopHoc = maLopHoc)
            return render(request,"editLopHoc.html",{"form":form,"id":maLopHoc,})
        
        
def edit_teacher(request,usernameTeacher):
    request.session['username']=usernameTeacher
    teacher=Teacher.objects.get(username=usernameTeacher)
    print(teacher.first_name)
    form=EditTeacherForm()
    form.fields['first_name'].initial=teacher.first_name
    form.fields['last_name'].initial=teacher.last_name
    form.fields['email'].initial=teacher.email
    form.fields['phoneNumber'].initial=teacher.phoneNumber
    form.fields['isGVCN'].initial=teacher.isGVCN

   
    return render(request,"editGiaoVien.html",{"form":form,"id":usernameTeacher,})

def edit_teacher_save(request):
    
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        usernameTeacher=request.session.get("username")
        
        print(usernameTeacher)
        form=AddTeacherForm(request.POST,request.FILES)
        
        if form.is_valid():
            first_name=form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            phoneNumber = form.cleaned_data["phoneNumber"]
            isGVCN = form.cleaned_data["isGVCN"]
            
            print(isGVCN)
          
            try:
                teacher =Teacher.objects.get(username = usernameTeacher)
                
                
                
                teacher.first_name = first_name
                teacher.last_name = last_name
                teacher.email = email
                teacher.phoneNumber = phoneNumber
                teacher.isGVCN = isGVCN
                
                teacher.save()
                messages.success(request,"Sửa thông tin giáo viên thành công")
                return HttpResponseRedirect(reverse("edit_teacher",kwargs={"usernameTeacher":usernameTeacher}))
            except:
                messages.error(request,"Lỗi Khi Sửa thông tin giáo viên")
                return HttpResponseRedirect(reverse("edit_teacher",kwargs={"usernameTeacher":usernameTeacher}))
        else:
            form=EditTeacherForm(request.POST)
            teacher =Teacher.objects.get(username = usernameTeacher)
            return render(request,"editGiaoVien.html",{"form":form,"id":usernameTeacher,})
        
def add_course(request):
    form=AddCourseForm()
    return render(request,"themMonHoc.html",{"form":form})


def add_course_save(request):
    
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        form=AddCourseForm(request.POST,request.FILES)
        
        if form.is_valid():
            tenMonHoc=form.cleaned_data["tenMonHoc"]
            moTa = form.cleaned_data["moTa"]
            maLopHoc = form.cleaned_data["maLopHoc"]
            
            try:
                newCourse = MonHoc(tenMonHoc = tenMonHoc, moTa = moTa,lopHoc_id = maLopHoc )
                print(newCourse)
                newCourse.save()
                messages.success(request,"Thêm Môn Học Mới Thành Công")
                return HttpResponseRedirect(reverse("add_course"))
            except:
                messages.error(request,"Lỗi Khi Thêm Môn Học Mới")
                return HttpResponseRedirect(reverse("add_course"))
        else:
            form=AddCourseForm(request.POST)
            return render(request, "themMonHoc.html", {"form": form})
        
def manage_course(request):
    courses=MonHoc.objects.all()
    print(courses[0].lopHoc.tenLopHoc)
    return render(request,"quanLyMonHoc.html",{"courses":courses})

def edit_course(request,maMonHoc):
    request.session['maMonHoc']=maMonHoc
    grade=MonHoc.objects.get(maMonHoc=maMonHoc)
    
    form=EditCourseForm()
    form.fields['tenMonHoc'].initial=grade.tenMonHoc
    form.fields['moTa'].initial=grade.moTa
    form.fields['maLopHoc'].initial=grade.lopHoc
   
    return render(request,"editMonHoc.html",{"form":form,"id":maMonHoc,})

def edit_course_save(request):
    
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        maMonHoc=request.session.get("maMonHoc")
        
        form=AddCourseForm(request.POST,request.FILES)
        
        if form.is_valid():
            tenMonHoc=form.cleaned_data["tenMonHoc"]
            moTa = form.cleaned_data["moTa"]
            
            maLopHoc = form.cleaned_data["maLopHoc"]
            
          
            try:
                course =MonHoc.objects.get(maMonHoc = maMonHoc)
                
                print(course)
                
                course.tenMonHoc = tenMonHoc
                course.moTa = moTa
                course.lopHoc_id = maLopHoc
       
                
                course.save()
                messages.success(request,"Sửa thông tin môn học thành công")
                return HttpResponseRedirect(reverse("edit_course",kwargs={"maMonHoc":maMonHoc}))
            except:
                messages.error(request,"Lỗi Khi Sửa thông tin môn học")
                return HttpResponseRedirect(reverse("edit_course",kwargs={"maMonHoc":maMonHoc}))
        else:
            form=EditCourseForm(request.POST)
            course =MonHoc.objects.get(maMonHoc = maMonHoc)
            return render(request,"editMonHoc.html",{"form":form,"id":maMonHoc,})