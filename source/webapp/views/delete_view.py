from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Task
from django.views.generic import TemplateView


class TaskDeleteView(TemplateView):
    template_name = 'delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, "delete.html", context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['task'].delete()
        return redirect('task_home')

