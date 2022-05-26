"""management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from giaovien import views as giaovien_views
from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from giaovien import studentViews



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', giaovien_views.DashboardView.as_view(),name='dashboard'),
    path("profile/", giaovien_views.ProfileEditView.as_view(), name='profile'),
    path("login/", giaovien_views.SiteLoginView.as_view(), name='login'),
    path("logout/", giaovien_views.SiteLogoutView.as_view(), name='logout'),
    path("quanlygiaovien", giaovien_views.QuanLyGiaoVienView.as_view(), name='quanlygiaovien'),
    path("themgiaovien/", giaovien_views.SiteAddNewGiaoVienView.as_view(), name='themgiaovien'),
    path("addNewGV/",giaovien_views.SiteAddNewGiaoVienView.as_view(),name='addNewGV'),
    path('add_student', studentViews.add_student,name="add_student"),
    path('add_student_save', studentViews.add_student_save,name="add_student_save"),
    path('quanlyhocsinh', studentViews.manage_student,name="manage_student"),
    path('edit_student/<str:student_id>', studentViews.edit_student,name="edit_student"),
    path('edit_student_save', studentViews.edit_student_save,name="edit_student_save"),
    path('add_grade', studentViews.add_grade,name="add_grade"),
    path('add_grade_save', studentViews.add_grade_save,name="add_grade_save"),
    path('quanlylophoc', studentViews.manage_grade,name="manage_grade"),
    path('edit_grade/<str:maLopHoc>', studentViews.edit_grade,name="edit_grade"),
    path('edit_grade_save', studentViews.edit_grade_save,name="edit_grade_save"),
    path('edit_teacher/<str:usernameTeacher>', studentViews.edit_teacher,name="edit_teacher"),
    path('edit_teacher_save', studentViews.edit_teacher_save,name="edit_teacher_save"),
    path('add_course', studentViews.add_course,name="add_course"),
    path('add_course_save', studentViews.add_course_save,name="add_course_save"),
    path('quanlymonhoc', studentViews.manage_course,name="manage_course"),
    path('edit_course/<str:maMonHoc>', studentViews.edit_course,name="edit_course"),
    path('edit_course_save', studentViews.edit_course_save,name="edit_course_save"),
    
    
] + static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)


