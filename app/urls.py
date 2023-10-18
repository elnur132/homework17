from django.urls import path
from .views import ListTasks, add_task,update_task, deleta_task

urlpatterns = [
    path('', ListTasks, name='tasks'),
    path('add/', add_task, name='add-task'),
    path('update/<int:id>', update_task, name='update-task'),
    path('delete/<int:id>', deleta_task, name='delete-task')
]
