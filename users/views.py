from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import *
from django.contrib.auth.decorators import login_required
from agv.models import *
from blocs.models import *
from commandes.views import sendCommand as newCommand
from commandes.forms import CommandeForm
from django.http import HttpResponse
from getmac import get_mac_address as gma
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
    return render(request,'admin/login.html', {
        'form': form
    })

# Renders the admin home page if the user is authenticated, otherwise redirects to the login form.
@require_GET
def adminIndex(request):
    if request.user.is_authenticated:
        context = {}
        context['agvs'] =  Agv.objects.all().count()
        context['blocs'] = Bloc.objects.all().count()
        context['postes'] = Poste.objects.all().count()
        return render(request, 'admin/home.html', context)
    else:
        return redirect('loginForm')
    
# Logout the admin from his account
@login_required
def adminLogout(request):
    logout(request)
    return redirect('loginForm')

@require_GET
def commande(request):
    form = CommandeForm()
    return render(request, 'commandes/send.html',{
        'form': form
    })

@require_POST
def sendCommand(request):
    form = CommandeForm(request.POST)
    isAuthenticated = request.user.is_authenticated
    macAddress = Poste.objects.filter(mac_address=gma()).first()
    if macAddress is not None or isAuthenticated :
        try :
            agv = request.POST.get('id_agv')
            bloc = request.POST.get('id_bloc')
            newCommand(agv, bloc)
            return HttpResponse('Agv sent')
        except Exception as e:
            print(e)
            return HttpResponse(e)
    else :
        return HttpResponse('Not allowed')
   