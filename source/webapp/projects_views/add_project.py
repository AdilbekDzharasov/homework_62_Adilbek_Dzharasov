from urllib import request
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import DetailView, CreateView, UpdateView
from webapp.forms import ProjectForm
from webapp.models.projects import Project
from webapp.forms import ProjectAddUserForm


class ProjectAddView(LoginRequiredMixin, CreateView):
    template_name = 'projects/add_project.html'
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class ProjectDetailView(DetailView):
    template_name = "projects/project.html"
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = self.object.tasks.order_by("-created_at")
        return context


class ProjectAddUserView(UpdateView):
    model = Project
    template_name = 'projects/projects_user_add.html'
    form_class = ProjectAddUserForm

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        user = form.save(commit=False)
        user.project = project
        user.save()
        form.save_m2m()
        return redirect('project_detail', pk=project.pk)

