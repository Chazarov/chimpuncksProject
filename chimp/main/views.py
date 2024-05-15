from django.shortcuts import render 
from django.http import HttpResponse
from task.models import Task

def show_archive(request):
    tasks = Task.objects.all()
    return render(request, "main/archive.html", {"tasks" : tasks})

def show_teacher(request):
    
    return render(request, "main/teacher.html")
    

