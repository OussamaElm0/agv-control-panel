from django.shortcuts import render, redirect
from .models import Poste
from .forms import AdminLoginForm
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.decorators import login_required
from agv.models import Agv
from blocs.models import Bloc
from commandes.views import sendCommand as newCommand
from commandes.forms import CommandeForm
from commandes.models import Commande
from django.http import HttpResponse
from getmac import get_mac_address as gma
from django.core.paginator import Paginator
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta
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
def dashboard(request):
    if request.user.is_authenticated:
        # Calculate the start and end dates for the last week
        end_date = timezone.now()
        start_date = end_date - timedelta(days=7)

        # Filter Commande objects for the last week
        commandes_last_week = Commande.objects.filter(date__gte=start_date, date__lte=end_date)

        # Group Commande objects by date and count the number of Commandes for each date
        commands_per_day_last_week = commandes_last_week.values('date').annotate(total_commandes=Count('id'))

        context = {
            'total_agvs': Agv.objects.all().count(),
            'total_blocs': Bloc.objects.all().count(),
            'total_postes': Poste.objects.all().count(),
            'commands_per_day_last_week': list(commands_per_day_last_week)
        }
        print(type  (commands_per_day_last_week))
        return render(request, 'admin/dashboard.html', context)
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
    isAuthenticated = request.user.is_authenticated
    macAddress = Poste.objects.filter(mac_address=gma()).first()
    if macAddress is not None or isAuthenticated :
        agvsToBloc = Commande.objects.filter(confirmed=False, id_bloc=macAddress.bloc).order_by('-id')
        paginator = Paginator(agvsToBloc,5)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context = {
            'form': form,
            'agvsToBloc': page_obj
        }
        return render(request, 'commandes/send.html',context)
    else :
        return render(request,'http_errors/401.html')

@require_POST
def sendCommand(request):
    isAuthenticated = request.user.is_authenticated
    macAddress = Poste.objects.filter(mac_address=gma()).first()
    if macAddress is not None or isAuthenticated :
        try :
            agv = request.POST.get('id_agv')
            bloc = request.POST.get('id_bloc')
            newCommand(agv, bloc)
            return redirect('/')
        except Exception as e:
            print(e)
            return HttpResponse(e)
    else :
        return HttpResponse('Not allowed')

@require_POST
def updateCommande(request, id):
    method = request.POST.get('method')
    if method == "PUT":
        commande = Commande.objects.get(pk=id)
        commande.confirmed =True
        commande.save()
    return redirect('/')