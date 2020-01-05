from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist


class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length = 50, help_text = "Enter your name")
	last_name = forms.CharField(max_length = 50, help_text = "Enter your name")
	email = forms.EmailField(help_text = "Enter your valid email address")

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if email:
			if User.objects.filter(email=email).exists():
				raise forms.ValidationError('Your email is not unique.')
		return email

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class LoginForm(forms.Form):
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput(render_value=False))


	def clean(self):
		user = self.authenticate_via_email()
		if not user:
			raise forms.ValidationError("sorry the login was invald")
		else:
			self.user = user
		return self.cleaned_data

	def authenticate_user(self):
		return authenticate(username=self.user.username, password=self.cleaned_data['password'])


	def authenticate_via_email(self):
		email = self.cleaned_data['email']
		if email:
			try:
				user = User.objects.get(email__iexact=email)
				if user.check_password(self.cleaned_data['password']):
					return user
			except ObjectDoesNotExist:
				pass
		return None