from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
from Apps.Student.models import Student
from Apps.Subject.models import Subject


class Enrollment(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'ACTIVE', 'Active'
        COMPLETED = 'COMPLETED', 'Completed'
        DROPPED = 'DROPPED', 'Dropped'

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='enrollments')
    academic_year = models.CharField(max_length=20, help_text="e.g. 2025-2026")
    semester = models.CharField(max_length=20, blank=True, null=True, help_text="e.g. Semester 1")
    enrollment_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE)

    class Meta:
        ordering = ['-enrollment_date']
        unique_together = ('student', 'subject', 'academic_year', 'semester')

    def __str__(self):
        return f"{self.student} -> {self.subject} ({self.academic_year})"

    def get_absolute_url(self):
        return reverse('enrollment:detail', kwargs={'pk': self.pk})
