from django.shortcuts import render, redirect, get_object_or_404
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
        'detail_description': request.POST.get('detail_description'),
        'status': request.POST.get('status'),
        'execute_at': execute
    }
    task = Task.objects.create(**task_data)
    return redirect('task_detail', pk=task.pk)


def detail_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task.html', context={'task': task})

