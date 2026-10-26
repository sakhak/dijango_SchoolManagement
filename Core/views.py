from django.contrib.auth.decorators import login_required
from django.shortcuts import render
''''
from Apps.Student.models import Student
from Apps.Teacher.models import Teacher
from Apps.Subject.models import Subject
from Apps.Attendance.models import Attendance
from Apps.Payment.models import Payment
from Apps.Examination.models import Exam
'''
import datetime


def home(request):
    context = {
        #'student_count': Student.objects.count(),
        #'teacher_count': Teacher.objects.count(),
        #'subject_count': Subject.objects.count(),
    }
    return render(request, 'core/home.html', context)


@login_required
def dashboard(request):
    today = datetime.date.today()
    context = {
        #'student_count': Student.objects.filter(status='ACTIVE').count(),
        #'teacher_count': Teacher.objects.filter(status='ACTIVE').count(),
        #'subject_count': Subject.objects.count(),
        #'today_attendance': Attendance.objects.filter(date=today).count(),
        #'pending_payments': Payment.objects.filter(status__in=['PENDING', 'OVERDUE']).count(),
        #'upcoming_exams': Exam.objects.filter(date__gte=today).order_by('date')[:5],
        #'recent_students': Student.objects.order_by('-created_at')[:5],
    }
    return render(request, 'core/dashboard.html', context)
