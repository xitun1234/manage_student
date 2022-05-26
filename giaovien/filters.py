import django_filters

from .models import *

class TeacherFilter(django_filters.FilterSet):
    

    class Meta:
        model = Teacher
        fields = ['last_name', 'isGVCN']