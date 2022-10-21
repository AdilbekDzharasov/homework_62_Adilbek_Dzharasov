from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, CreateView
from webapp.forms import ProjectForm
from webapp.models.projects import Project


class ProjectAddView(LoginRequiredMixin, CreateView):
    template_name = 'projects/add_project.html'
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class ProjectDetailView(LoginRequiredMixin, DetailView):
    template_name = "projects/project.html"
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = self.object.tasks.order_by("-created_at")
        return context

