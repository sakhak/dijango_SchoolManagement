from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Enrollment


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'academic_year', 'semester', 'status', 'enrollment_date')
    list_filter = ('status', 'academic_year', 'semester')
    search_fields = ('student__first_name', 'student__last_name', 'subject__name')
