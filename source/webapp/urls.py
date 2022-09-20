from django.urls import path
from webapp.views.base import home_view

urlpatterns = [
    path('', home_view)
]