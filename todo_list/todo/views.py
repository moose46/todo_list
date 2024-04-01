from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task

    
class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    
#...  
class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'

# ...
   


def home(request):
    print("home(request)")
    return render(request, "home.html")

