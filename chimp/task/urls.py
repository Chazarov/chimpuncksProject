from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_task),
    path('create', views.show_task_edditor),
]