from django.shortcuts import render
from .models import *
from .forms import *

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
            admin = Admin.objects.filter(username=username, password=password)
            if admin.exists():
                return render(request, 'users/admin/home.html')
            else:
                return render(request, 'users/admin/login.html', {'form': form})
        else:
            return render(request, 'users/admin/login.html', {'form': form})