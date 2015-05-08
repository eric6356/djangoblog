from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_user
from django.contrib.auth import logout as logout_user


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {'form': AuthenticationForm()})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login_user(request, user)
            return render(request, 'index.html')

def logout(request):
    logout_user(request)
    return render(request, 'index.html')
