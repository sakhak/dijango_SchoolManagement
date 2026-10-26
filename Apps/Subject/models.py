from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
from Apps.Teacher.models import Teacher


class Subject(models.Model):
    subject_name = models.CharField(max_length=150)
    subject_code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True, null=True)
    credit_hours = models.PositiveIntegerField(default=1)
    teacher = models.ForeignKey(
        Teacher, on_delete=models.SET_NULL, null=True, blank=True, related_name='subjects'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['subject_name']

    def __str__(self):
        return f"{self.subject_code} - {self.subject_name}"

    def get_absolute_url(self):
        return reverse('subject:detail', kwargs={'pk': self.pk})
