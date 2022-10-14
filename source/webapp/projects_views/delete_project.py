from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from webapp.models.projects import Project
from django.views.generic import DeleteView


def confirm_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.delete_project()
    return redirect('project_home')


class ProjectDeleteView(DeleteView):
    template_name = 'projects/delete_projects.html'
    model = Project
    context_object_name = 'project'
    success_url = reverse_lazy('project_home')

