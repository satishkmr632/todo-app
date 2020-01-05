from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from todo.models import Task, Activity
from .forms import CreateTaskForm
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url = 'account:login')
def all_tasks(request):
	user = request.user
	user_tasks = Task.objects.filter(Task_user__username = user).order_by('-Task_added_at')
	# for task in user_tasks:
	# 	if request.method == 'POST':
	# 		user_task_form = CreateTaskForm(instance = task)
	# 		if user_task_form.is_valid():
	# 			test1 = user_task_form.cleaned_data.get('Task_completed')
	# 			test1.save(commit = False)
	# 			test1.Task_completed = True
	# 			# print(test1)
	# 			test1.save(commit = True)


	context = {
		'user_tasks': user_tasks,
		# 'user_task_form': user_task_form
	}
	return render(request, 'todo/task_list.html', context)


@login_required(login_url = 'account:login')
def create_task(request):
	if request.method == 'POST':
		task_form = CreateTaskForm(request.POST)
		if task_form.is_valid():
			# print(task_form.cleaned_data.as_json())
			task_form = task_form.save(commit = False)
			task_form.Task_user = request.user
			task_form.save()
			# task_form.cleaned_data.get('Task_name')
			Activity.objects.create(user = request.user, activity_type = 'A', task = task_form)
			return redirect('/')
	else:
		task_form = CreateTaskForm()
		# print(task_form.cleaned_data[])
	return render(request, 'todo/new_task.html', {'task_form': task_form})


@login_required(login_url = 'account:login')
def task_detail(request, task_id):
	task_instance = get_object_or_404(Task, id = task_id)
	context = {
		'task_instance': task_instance,
	}
	return render(request, 'todo/task_detail.html', context)


@login_required(login_url = 'account:login')
def update_task(request, task_id):
	task_id = int(task_id)
	try:
		task_instance = Task.objects.get(id = task_id)
	except Task.DoesNotExist:
		return redirect('/')


	if request.method == 'POST':
		task_form = CreateTaskForm(request.POST, instance = task_instance)
		if task_form.is_valid():
			task_form.save()
			return redirect('/')
	else:
		data = {'Task_name': task_instance.Task_name, 'Task_deadline': task_instance.Task_deadline, 'Task_completed': task_instance.Task_completed}
		task_form = CreateTaskForm(initial = data)
	return render(request, 'todo/task_edit.html', {'task_form': task_form})


@login_required(login_url = 'account:login')
def delete_task(request, task_id):
	task_instance = get_object_or_404(Task, id = task_id)
	Activity.objects.create(user = request.user, activity_type = 'D', task = task_instance)
	task_instance.delete()
	return redirect('/')

# def complete_multiple_task(request task_id):
# 	incomplete_task = get_object_or_404(id = task_id)
# 	if request.method == 'POST':


@login_required(login_url = 'account:login')
def completed_tasks(request):
	all_completed_tasks = Task.objects.filter(Task_user = request.user, Task_completed = True).order_by('-Task_added_at')
	print(all_completed_tasks)
	return render(request, 'todo/completed_tasks.html', {'all_completed_tasks': all_completed_tasks})


@login_required(login_url = 'account:login')
def incompleted_tasks(request):
	all_incompleted_tasks = Task.objects.filter(Task_user = request.user, Task_completed = False).order_by('-Task_added_at')
	return render(request, 'todo/incompleted_tasks.html', {'all_incompleted_tasks': all_incompleted_tasks})


@login_required(login_url = 'account:login')
def activity_feed(request):
	recent_activities_by_user = Activity.objects.filter(user = request.user).order_by('-date')

	context = {
		'recent_activities_by_user':recent_activities_by_user,
	}
	return render(request, 'todo/activity.html', context)
