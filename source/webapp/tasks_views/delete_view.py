from django.urls import reverse_lazy
from webapp.models import Task
from django.views.generic import DeleteView


class TaskDeleteView(DeleteView):
    template_name = 'tasks/delete.html'
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('task_home')

