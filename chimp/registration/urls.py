from django.urls import path
from .views import show_reg


urlpatterns = [
    path('', show_reg, name = "registration")
]