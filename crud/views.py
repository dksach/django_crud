from django.shortcuts import render,redirect
from . models import Teacher
from . models import Student

def index(request):
    return render(request,'index.html')

def student(request):
    return render(request,'student.html')

def upload(request):
    if request.method=='POST':
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        course = request.POST.get('course')
        age = request.POST.get('age')
        Student.objects.create(name=name,age=age,gender=gender,course=course)
        return render(request,'thankyou.html')
    else:
        return redirect('/')

def insert(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        Teacher.objects.create(name=name,email=email)
        return render(request,'thankyou.html')
    else:
        return redirect('/')
