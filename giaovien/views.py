from audioop import reverse
from http.client import HTTPResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views import View
from giaovien.forms import ThemGiaoVienForm
from django.http import HttpResponse
from giaovien.filters import TeacherFilter
from .models import Teacher

User = get_user_model()

class DashboardView(TemplateView):
    template_name = "pages/home.html"
    
    
class SiteLoginView(LoginView):
    template_name = "login.html"

class EditProfileView(LoginRequiredMixin,TemplateView):
    template_name = "profile.html"


class SiteLogoutView(LogoutView):
    template_name = "pages/home.html"
    
class ProfileEditView(LoginRequiredMixin,UpdateView):
    template_name = 'profile.html'
    model = User 
    print("helo")
    fields = ('first_name','last_name','diaChi','phoneNumber')
    success_url = reverse_lazy("profile")
    
    def get_object(self, queryset = None):
        print(self.request.user)
        return self.request.user
    
class QuanLyGiaoVienView(View):
    def get(self,request):
        DataGiaoVien = Teacher.objects.all()
        print(DataGiaoVien)
        
        myFilter = TeacherFilter(request.GET,queryset = DataGiaoVien)
        DataGiaoVien = myFilter.qs 
        
        context = {'DataGiaoVien':DataGiaoVien,'myFilter': myFilter}
        print(context)
        
        return render(request,'quanlyGiaoVien.html', context)
    

class FormGiaoVienClass(View):
    def get(self,request):
        a = ThemGiaoVienForm()
        return render(request,'themGiaoVien.html', {'f' : a})
    

class ClassSaveGiaoVienMoi(View):
    def post(self,request):
        g = ThemGiaoVienForm(request.POST)
        print(g.cleaned_data)
        
        if g.is_valid():
            g.save()
             
        else:
            return HttpResponse('sai du lieu')
        

class AddGiaoVienForm(UserCreationForm):
    
    class Meta:
        model = Teacher
        fields = ('username','email','first_name','last_name','phoneNumber','isGVCN')
        
class SiteAddNewGiaoVienView(FormView):
    template_name = 'themGiaoVien.html'
    form_class = AddGiaoVienForm
    
    def form_valid(self, form):
        data = form.cleaned_data
        print(data)
        
        new_GiaoVien = User.objects.create_user(
            username = data['username'],
            password = data['password1'],
            email = data['email'],
            first_name = data['first_name'],
            last_name = data['last_name'],
            phoneNumber = data['phoneNumber'],
            isGVCN = data['isGVCN'],
        )
        
        return HttpResponse('Lưu Thành Công')
    