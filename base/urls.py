from django.urls import path
from .views import TaskList,  TaskDetail, TaskCreate
from .models import Task


urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
     path('create-task/', TaskCreate.as_view(), name='task-create'),
    ]
