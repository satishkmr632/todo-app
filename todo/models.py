from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# from django.db.models.signals import pre_delete
# from django.dispatch import receiver
# from todo.views import 

# Create your models here.

class Task(models.Model):
	Task_name = models.CharField(max_length = 100)
	Task_deadline = models.DateField(auto_now = False)
	Task_completed = models.BooleanField(default = False)
	Task_user = models.ForeignKey(User, on_delete = models.CASCADE)
	Task_added_at = models.DateTimeField(auto_now = True)


	def __str__(self):
		return self.Task_name

	class Meta:
		ordering = ('-Task_deadline',)
		verbose_name = 'Task'


	# def task_status(self):
	# 	if self.Task_completed == False:
	# 		return self.Task_completed == True
	# 	else:
	# 		return self.Task_completed == False




class Activity(models.Model):
	Add = 'A'
	Delete = 'D'
	Complete = 'C'
	Incomplete = 'I'

	ACTIVITY_TYPES = (
		(Add, 'add task'),
		(Delete, 'delete task'),
		(Complete, 'complete task'),
		(Incomplete, 'incomplete task'),

	)
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	activity_type = models.CharField(max_length = 1, choices = ACTIVITY_TYPES)
	task = models.CharField(max_length = 100, null = True)
	date = models.DateTimeField(auto_now = True)

	# def __str__(self):
	# 	if self.activity_type == 'Add':
	# 		return "you have created a task {}".format(self.task)
	# 	elif self.activity_type == 'Delete':
	# 		return "you have deleted a task {}".format(self.task)


	class Meta:
		ordering = ('-date',)
		verbose_name = 'Activitie'



# @receiver(pre_delete, sender = Task)
# def handle_delete_task(**kwargs):
# 	task = kwargs['instance']
# 	delete_activity = Activity.objects.filter(task = task)











