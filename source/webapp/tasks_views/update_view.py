from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import UpdateView
from webapp.models import Task
from webapp.forms import TaskForm


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'tasks/update.html'
    form_class = TaskForm
    model = Task
    context_object_name = 'task'

    def get_success_url(self):
        return reverse('task_detail', kwargs={'pk': self.object.pk})

