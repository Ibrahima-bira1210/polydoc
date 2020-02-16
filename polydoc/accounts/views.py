from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import UserloginForm
from django.contrib.auth import authenticate, login, logout


# from .filters import OrderFilter
# Create your views here.
def home(request):
    return render(request, 'accounts/index.html')


# view pour la connection

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('yes successful')
            else:
                return HttpResponse('not active')
        else:
            return HttpResponse('user is none')
    else:
        return render(request, 'accounts/login.html')

# logout

def user_logout(request):
    logout(request)
    return redirect('home')


# view pour gerer l'inscription


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        choice = request.POST['choice']
        user = User()
        profile = Profil()
        user.is_active = False
        user.username = username
        user.email = email
        user.password = password
        user.save()
        profile.profil_user = user
        profile.save()
        if choice == 'eleve':
            eleve = Eleve()
            eleve.eleve_user = user
            eleve.save()
        else:
            prof = Prof()
            prof.prof_user = user
            prof.save()

        return render(request, 'accounts/profil.html', {'user':user})
    else:
        classes = Classe.objects.all()
        return render(request,'accounts/register.html',{'classes': classes})


# mon profil

def profile(request):
    return render(request,'account/profil.html')
