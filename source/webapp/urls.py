from django.urls import path
from webapp.views.base import home_view
from webapp.views.add import add_view, detail_view

urlpatterns = [
    path('', home_view, name='task_home'),
    path('tasks/add/', add_view, name='task_add'),
    path('tasks/<int:pk>', detail_view, name='task_detail')
]

