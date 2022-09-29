from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Task


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'task': task})
    elif request.method == 'POST':
        task.delete()
        return redirect('task_home')

