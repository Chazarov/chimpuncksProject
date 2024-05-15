from django.contrib import admin
from .models import Task, Test, Resolve

admin.site.register(Task)
admin.site.register(Test)
admin.site.register(Resolve)