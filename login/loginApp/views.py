from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .forms import RegistrationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import Http404

def not_found_view(request):
    return render(request, '404.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RegistrationForm()
    
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})

def index(request):
    return render(request, 'index.html')

def logout_views(request):
    logout(request)
    return redirect('index')

@login_required(login_url='login')
def dashboard(request):
    username = request.user.username
    show_popup = True
    return render(request,'dashboard.html', {'username': username,'show_popup': show_popup})