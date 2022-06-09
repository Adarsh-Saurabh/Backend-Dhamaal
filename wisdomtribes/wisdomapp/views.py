from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request, 'templates/about.html')

def contact(request):
    return render(request, 'templates/contact.html')

def services(request):
    return render(request, 'templates/services.html')

def courses(request):
    return render(request, 'templates/courses.html')

def online_courses(request):
    return render(request, 'templates/online_courses.html')

def login(request):
    # CLearing Session on logout
    request.session = {}
    return render(request, 'login.html', {"msg": ""})

def indtutor(request):
    return render(request, 'teacherRegistration.html')

def studentRegistration(request):
    return render(request, 'studentRegistration.html')
