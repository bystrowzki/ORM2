from django.views.generic import ListView
from django.shortcuts import render, redirect
from .models import Teacher
from .models import Student


def index(request):
    return redirect('school/students_list/')


def students_list(request):
    template = 'school/students_list.html'
    all_students = Student.objects.all()
    context = {'students': all_students,
               }

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    return render(request, template, context=context)


def show_teachers(request):
    template = 'school/students_list.html'
    all_teachers = Teacher.objects.all()
    context = {'teachers': all_teachers}
    return render(request, template, context=context)
