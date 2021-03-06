from django.urls import path
from .views import TaskList,  TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView
from .models import Task
from django.contrib.auth.views import LogoutView

urlpatterns = [
     path('login/', CustomLoginView.as_view(), name='login'),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('create-task/', TaskCreate.as_view(), name='create-task'),
    path('update-task/<int:pk>/', TaskUpdate.as_view(), name='update-task'),
    path('delete-task/<int:pk>/', TaskDelete.as_view(), name='delete-task'),
    ]
