from django.urls import path, include
from account.views import sign_up, login_request, logout_request


app_name = 'account'
urlpatterns = [
    path('sign-up/', sign_up, name = 'sign_up'),
    path('login/', login_request, name = 'login'),
    path('logout/', logout_request, name = 'logout'),
]
