from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from webapp.models import Task
from webapp.forms import TaskForm
from django.views.generic.detail import DetailView


class TaskAddView(TemplateView):
    template_name = 'add.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = TaskForm()
        context['form'] = form
        return render(request, "add.html", context={'form': form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = form.save()
            return redirect('task_detail', pk=task.pk)
        else:
            return render(request, "add.html", context={'form': form})


class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'task.html'

