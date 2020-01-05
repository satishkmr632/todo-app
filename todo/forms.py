from django import forms
from .models import Task
from django.conf import settings

class CreateTaskForm(forms.ModelForm):
	Task_deadline = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)

	class Meta:
		model = Task
		fields = ('Task_name', 'Task_deadline', 'Task_completed')