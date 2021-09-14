from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


# Create your views here.
class TaskList(ListView):
    model = Task
    context_object_name = "tasks"
 
 
class TaskDetail(DetailView):
    model = Task
    context_object_name = "task" 
    template_name = "base/task_detail.html"
    
    
class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
