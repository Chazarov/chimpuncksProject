from django.shortcuts import render, redirect#Перемещает пользователя на другую страницу

from .models import Task, Resolve
from .forms import ResolveForm
from .compi import checkTask

import datetime

def show_task_edditor(request):
    return render(request, "task/create_task.html")

def show_task(request):
    solves = Resolve.objects.all()
    error = ""
    
    if request.method == "POST":
        form = ResolveForm(request.POST)
        


        if form.is_valid():
            new_record = form.save(commit=False)
            new_record.decision_status = form.cleaned_data['decision_status']

            
                
            new_record.decision_status = checkTask(form.cleaned_data['resolve'], "check","7,8","15")

            new_record.resolve_date = form.cleaned_data['resolve_date']
            new_record.task_id = form.cleaned_data['task_id']
            new_record.user_id = form.cleaned_data['user_id']
            new_record.resolve_date = str(datetime.datetime.now())[:-10]
            new_record.task_id = "N1"
            new_record.user_id = "N1"
            new_record.save()
        else:
            print(form.errors)
            error = "Форма была неверной"

        

        


    form = ResolveForm()
    context = {
        'form': form,
        'error': error,
        'solves': solves,
    }
    return render(request, 'task/task.html', context)
