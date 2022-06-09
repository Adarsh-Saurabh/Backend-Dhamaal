from django.urls import path
from . import views

urlpatterns = [
    path('add_teachers/', views.add_teacher_entry),
    path('add_students/', views.add_student_entry)
]
