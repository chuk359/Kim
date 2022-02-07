from django.db.models import fields
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm




def index(request):
    return render(request, 'main/index.html')

def takepart(request):
    error = ' '
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/present')
        else:
            error = "Try again. You made mistake in form"
    form = TaskForm()
    context = {'form': form}
    return render(request, 'main/takepart.html', context)

def present(request):
    tasks = Task.objects.order_by('-id')[1:2]
    return render(request, 'main/present.html', {'title': 'Present', 'tasks': tasks})


        
 
   
