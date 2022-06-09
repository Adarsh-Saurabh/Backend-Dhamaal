"""wisdomtribes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from wisdomapp import views
from teachers import views_teachers
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views_teachers.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("services/", views.services, name="services"),
    path("courses/", views.courses, name="courses"),
    path("onile_courses/", views.online_courses, name="online_courses"),
    path('add_teachers', views_teachers.add_teacher_entry),
    path('add_students', views_teachers.add_student_entry),
    path('login/', views.login),
    path('indtutor/', views.indtutor),
    path('studentRegistration', views.studentRegistration),
    path('loggingin', views_teachers.login),
    path('find_teachers', views_teachers.fetching_available_teacher_as_per_location),
    path('validation', views_teachers.validator),
    path('validation2', views_teachers.validator2),
    path('connected', views_teachers.student_teacher_connection),
    path('subscription-plan', views_teachers.subscription_request),
    path('student-home', views_teachers.studentHomePage),
    path('teacher-home', views_teachers.teacherHomePage),
    path('home',views_teachers.home),
    path('<str:room>/', views_teachers.chat, name = 'chat'),
    path('checkview', views_teachers.checkview, name = 'checkview'),
    path('send', views_teachers.send, name='send'),
    path('getMessages/<str:room>/', views_teachers.getMessages, name='getMessages')
    # path('chat', views_teachers.chat, name = 'chat')
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
