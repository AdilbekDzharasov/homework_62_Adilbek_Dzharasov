from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Task
from webapp.forms import TaskForm


def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        form = TaskForm(initial={
            'description': task.description,
            'detail_description': task.detail_description,
            'status': task.status,
            'execute_at': task.execute_at
        })
        return render(request, 'update.html', context={'form': form, 'task': task})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.description = form.cleaned_data['description']
            task.detail_description = form.cleaned_data['detail_description']
            task.status = form.cleaned_data['status']
            task.execute_at = form.cleaned_data['execute_at']
            task.save()
            return redirect('task_detail', pk=task.pk)
        else:
            return render(request, 'update.html', context={'form': form, 'task': task})

