from django.urls import path
from todo import views

app_name = 'todo'
urlpatterns = [
    path('', views.all_tasks, name = 'all_tasks'),
    path('create-task', views.create_task, name = 'create-task'),
    path('task-detail/<int:task_id>', views.task_detail, name = 'task-detail'),
    path('task-edit/<int:task_id>', views.update_task, name = 'edit-task'),
    path('task-delete/<int:task_id>', views.delete_task, name = 'delete-task'),
    path('tasks-completed', views.completed_tasks, name = 'tasks-completed'),
    path('tasks-incompleted', views.incompleted_tasks, name = 'tasks-incompleted'),
    path('task-activity', views.activity_feed, name = 'task-activity-feed'),
]
