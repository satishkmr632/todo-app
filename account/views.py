from django.shortcuts import render, redirect, HttpResponse, reverse
from account.forms import SignUpForm, LoginForm
from django.contrib.auth import login, authenticate, logout


# Create your views here.

def sign_up(request):
	if request.method == 'POST':
		user_form = SignUpForm(request.POST)
		
		if user_form.is_valid():
			user_form.save(commit = True)
			print(user_form)
			username = user_form.cleaned_data.get('username')
			user_password = user_form.cleaned_data.get('password1')
			user_instance = authenticate(username = username, password = user_password)
			login(request, user_instance)
			return redirect('/')
	else:
		user_form = SignUpForm()
	return render(request, 'account/sign_up.html', {'user_form': user_form})


def login_request(request):
    form = LoginForm(request.POST or None)    
    if request.method == 'POST' and form.is_valid():
        user = form.authenticate_user()
        login(request, user)
        return redirect('/')

    return render(request, 'account/login.html',{'form': form})


def logout_request(request):
	logout(request)
	return redirect('/')