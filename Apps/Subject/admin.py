from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Subject


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_name', 'subject_code', 'teacher', 'credit_hours')
    list_filter = ('subject_code',)
    search_fields = ('subject_name', 'subject_code')
