from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
def adminLogin(request):
   if request.method == 'GET':
        form = AdminLoginForm()
        return render(request, 'users/admin/login.html', {'form': form})
   else :
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try :
                user = User.objects.get(username=username, password=password)
                print(user)
                admin = authenticate(request,username=username, password=password)
                print(admin)
                if admin is not None:
                    # User authentication successful
                    login(request, admin)
                    return render(request, 'users/admin/home.html')
                else:
                    # User authentication failed
                    error_message = 'Invalid username or password.'
                    return render(request, 'users/admin/login.html', {'form': form, 'error_message': error_message})
            except User.DoesNotExist:
                error_message = 'Invalid username or password.'
                return render(request, 'users/admin/login.html', {'form': form, 'error_message': error_message})
        else:
            print(form.errors)
            return render(request, 'users/admin/login.html', {'form': form})

def test(request):
    return render(request, 'users/admin/home.html')