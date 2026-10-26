from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'first_name', 'last_name', 'grade_level', 'section', 'status', 'admission_date')
    list_filter = ('status', 'grade_level', 'gender')
    search_fields = ('student_id', 'first_name', 'last_name', 'email')
    ordering = ('last_name','first_name')
