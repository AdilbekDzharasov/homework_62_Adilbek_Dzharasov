from django.urls import path
from webapp.views.base import home_view
from webapp.views.add import add_view, detail_view

urlpatterns = [
    path('', home_view),
    path('tasks/add/', add_view),
    path('tasks/', detail_view)
]

