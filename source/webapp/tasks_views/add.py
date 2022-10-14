from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView
from webapp.models import Task
from webapp.forms import TaskForm
from django.views.generic.detail import DetailView
from webapp.models.projects import Project
from webapp.forms import ProjectTaskForm


class TaskAddView(CreateView):
    model = Task
    template_name = 'tasks/add.html'
    form_class = TaskForm

    def get_success_url(self):
        return reverse('task_detail', kwargs={'pk': self.object.pk})


class ProjectTaskAddView(CreateView):
    model = Task
    template_name = 'tasks/project_task_add.html'
    form_class = ProjectTaskForm

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        task = form.save(commit=False)
        task.project = project
        task.save()
        form.save_m2m()
        return redirect('project_detail', pk=project.pk)


class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/task.html'

