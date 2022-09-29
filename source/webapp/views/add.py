from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Task
from webapp.forms import TaskForm


def add_view(request):
    if request.method == "GET":
        form = TaskForm()
        return render(request, "add.html", context={'form': form})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = Task.objects.create(
                description=form.cleaned_data['description'],
                detail_description=form.cleaned_data['detail_description'],
                status=form.cleaned_data['status'],
                execute_at=form.cleaned_data['execute_at']
            )
            return redirect('task_detail', pk=task.pk)
        else:
            return render(request, 'add.html', context={'form': form})


def detail_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task.html', context={'task': task})

