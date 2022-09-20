from django.shortcuts import render
from webapp.models import Task


def home_view(request):
    tasks = Task.objects.all()
    context = {
        "tasks": tasks
    }
    return render(request, "home.html", context)

