from django.urls import path
from .views import TaskList
from .models import Task


urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    ]
