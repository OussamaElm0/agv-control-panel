from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import *
from django.contrib.auth.decorators import login_required
from agv.models import *
from blocs.models import *

# Create your views here.

#View function to check if the user is an admin and handle the login process.
def checkIfAdmin(request):
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid: 
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('adminIndex')
            else :
                return render(request,'users/admin/login.html', {
                    'form': form,
                    'error_message': 'Username or password invalid'
                })
        return  render(request,'users/admin/login.html', {
                    'form': form,
                    'error_message': 'Form fields not valid'
                })
    elif request.user.is_authenticated:
        return redirect('adminIndex')
    form = AdminLoginForm()
    return render(request,'users/admin/login.html', {
        'form': form
    })

# Renders the admin home page if the user is authenticated, otherwise redirects to the login form.
@require_GET
def adminIndex(request):
    if request.user.is_authenticated:
        context = {}
        agvs = Agv.objects.all().count()
        context['agvs'] = agvs
        return render(request, 'users/admin/home.html', context)
    else:
        return redirect('loginForm')