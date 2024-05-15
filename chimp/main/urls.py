from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_archive, name = "archive"),
    path('teacher', views.show_teacher, name = "teacher"),
]