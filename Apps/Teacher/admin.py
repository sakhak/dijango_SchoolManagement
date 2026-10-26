from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher_id', 'first_name', 'last_name', 'specialization', 'status', 'joining_date')
    list_filter = ('status', 'specialization', 'gender')
    search_fields = ('teacher_id', 'first_name', 'last_name', 'email')
