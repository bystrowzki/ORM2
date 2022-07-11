from django.contrib import admin

from .models import Student, Teacher, Students_Teachers


class StudentsTeachersInline(admin.TabularInline):
    model = Students_Teachers
    extra = 0


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'group']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject']
    inlines = [StudentsTeachersInline, ]