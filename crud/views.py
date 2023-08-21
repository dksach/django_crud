from django.shortcuts import render,redirect
from . models import Teacher
from . models import Student

def index(request):
    data={
        
        'teachersData':Student.objects.all()
    }
    return render(request,'index.html',data)

def student(request):
    adata={
        'studentsData':Student.objects.all(),
    }
    return render(request,'student.html',adata)

def upload(request):
    if request.method=='POST':
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        course = request.POST.get('course')
        age = request.POST.get('age')
        Student.objects.create(name=name,age=age,gender=gender,course=course)
        return redirect('/')
    else:
        return redirect('/')

def insert(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        Teacher.objects.create(name=name,email=email)
        return redirect('/')
    else:
        return redirect('/')
