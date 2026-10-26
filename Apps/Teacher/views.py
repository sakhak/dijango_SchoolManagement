from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import Teacher
from .forms import TeacherForm
'''
def teacher_list(request):
    return  render(request,'teacher/teacher_list.html')

def teacher_detail(request):
    return render(request, 'teacher/teacher_detail.html')

def teacher_create(request):
    return render(request, 'teacher/teacher_form.html',)

def teacher_update(request):
    return render(request, 'teacher/teacher_form.html')

def teacher_delete(request):
    return render(request, 'teacher/teacher_confirm_delete.html')
'''

def teacher_list(request):
    query = request.GET.get('q', '')
    teachers = Teacher.objects.all()

    if query:
        teachers = teachers.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(teacher_id__icontains=query) |
            Q(specialization__icontains=query)
        )

    return render(request, 'teacher/teacher_list.html', {
        'teachers': teachers,
        'query': query,
        'Status': Teacher.Status,
    })

def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    return render(request, 'teacher/teacher_detail.html',
                  {'teacher': teacher})

def teacher_create(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            teacher = form.save()
            messages.success(request, f"Teacher {teacher.get_full_name()} added successfully.")
            return redirect('teacher:detail', pk=teacher.pk)
    else:
        form = TeacherForm()
    return render(request, 'teacher/teacher_form.html', {'form': form, 'title': 'Add Teacher'})

def teacher_update(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES, instance=teacher)
        if form.is_valid():
            form.save()
            messages.success(request, "Teacher updated successfully.")
            return redirect('teacher:detail', pk=teacher.pk)
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'teacher/teacher_form.html',
                  {'form': form, 'title': 'Edit Teacher'})


def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        name = teacher.get_full_name()
        teacher.delete()
        messages.success(request, f"Teacher {name} deleted successfully.")
        return redirect('teacher:list')
    return render(request, 'teacher/teacher_confirm_delete.html',
                  {'teacher': teacher})
