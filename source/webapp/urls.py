from django.urls import path
from webapp.views.base import home_view
from webapp.views.add import add_view, detail_view
from webapp.views.delete_view import delete_task
from webapp.views.update_view import update_task


urlpatterns = [
    path('', home_view, name='task_home'),
    path('tasks/add/', add_view, name='task_add'),
    path('tasks/delete/<int:pk>', delete_task, name='task_delete'),
    path('tasks/update/<int:pk>', update_task, name='task_update'),
    path('tasks/<int:pk>', detail_view, name='task_detail')
]

