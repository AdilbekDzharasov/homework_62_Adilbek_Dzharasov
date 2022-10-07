from django.urls import path
from webapp.views.base import HomeView
from webapp.views.add import TaskAddView, TaskDetailView
from webapp.views.delete_view import TaskDeleteView
from webapp.views.update_view import TaskUpdateView



urlpatterns = [
    path('', HomeView.as_view(), name='task_home'),
    path('tasks/add/', TaskAddView.as_view(), name='task_add'),
    path('tasks/delete/<int:pk>', TaskDeleteView.as_view(), name='task_delete'),
    path('tasks/update/<int:pk>', TaskUpdateView.as_view(), name='task_update'),
    path('tasks/<int:pk>', TaskDetailView.as_view(), name='task_detail')
]


