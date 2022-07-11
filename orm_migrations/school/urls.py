from django.urls import path

from school.views import students_list, index, show_teachers

urlpatterns = [
    path('', index),
    path('school/students_list/', students_list, name='students'),
    path('school/students_list/', show_teachers, name='students')
]
