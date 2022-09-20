from django.shortcuts import render, redirect
from webapp.models import Task


def add_view(request):
    if request.method == "GET":
        return render(request, "add.html")
    if request.POST.get('execute_at') == '':
        execute = None
    else:
        execute = request.POST.get('execute_at')
    task_data = {
        'description': request.POST.get('description'),
        'status': request.POST.get('status'),
        'execute_at': execute
    }
    task = Task.objects.create(**task_data)
    return redirect(f"/tasks/?pk={task.pk}")

def detail_view(request):
    pk = request.GET.get("pk")
    task = Task.objects.get(pk=pk)
    return render(request, 'task.html', context={'task': task})

