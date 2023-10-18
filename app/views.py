from django.shortcuts import redirect, render
from .models import Task

# Create your views here.
def ListTasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {'tasks':tasks})

def add_task(request):
    if request.method == "POST":
        task = request.POST
        add = Task.objects.create(name=task['name'], description=task['description'], date=task['date'])
        add.save()
        return redirect('tasks')
    else:
        return render(request, 'add_task.html')
    
def update_task(request, id):
    task = Task.objects.get(id=id)
    
    if request.method == 'POST':
        updated_task = request.POST
        task.name = updated_task['name']
        task.description = updated_task['description']
        task.date = updated_task['date']
        
        task.save()
        return redirect('tasks')
    else:
        return render(request, 'update_task.html', {'task':task})
    
def deleta_task(request, id):
    task = Task.objects.get(id=id)
    
    task.delete()
    return redirect('tasks')