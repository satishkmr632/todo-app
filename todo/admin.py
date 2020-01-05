from django.contrib import admin
from .models import Task, Activity
from django.contrib.admin.models import LogEntry

# Register your models here.

admin.site.register(Task)
admin.site.register(LogEntry)
admin.site.register(Activity)