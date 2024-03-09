from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.http import *

# Create your views here.
@require_GET
def loginForm(request):
    if request.method == 'GET':
        form = AdminLoginForm()
        return render(request, 'users/admin/login.html', {'form': form})

@require_POST
def checkIfAdmin(request):
    # if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse('logged_in_message')
    else:
            # Handle invalid login credentials
        error_message = "Invalid username or password."
        return HttpResponseRedirect('login', {'error_message': error_message})
