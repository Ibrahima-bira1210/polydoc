from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import mat_ens, DocForm
from .models import *


# from .filters import OrderFilter
# Create your views here.
def home(request):
    return render(request, 'accounts/index.html')


def choice_register(request):
    return render(request, 'accounts/choice_register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('ged')
            else:
                return HttpResponse('not active')
        else:
            return HttpResponse('user is none')
    else:
        return render(request, 'accounts/login.html')


# view pour gerer l'inscription


def register_eleve(request):
    classes = Classe.objects.all()
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        bio = request.POST['bio']
        photo = request.FILES['photo']
        classe = request.POST['classe']
        user = User()
        user.is_active = True
        user.last_name = lastname
        user.first_name = firstname
        user.email = email
        user.username = username
        user.set_password(password)
        user.save()

        classe_e = Classe.objects.get(nom_classe=classe)

        eleve = Eleve()
        eleve.eleve_user = user
        eleve.class_eleve = classe_e
        eleve.bio = bio
        eleve.photo = photo
        eleve.save()
        return redirect('user_login')
    else:
        context = {
            'classes': classes,
        }
        return render(request, 'accounts/register_eleve.html', context)


def register_prof(request):
    matiere = Matiere.objects.all()
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        bio = request.POST['bio']
        photo = request.FILES['photo']
        form = mat_ens
        form.save()
        user = User()
        user.is_active = True
        user.last_name = lastname
        user.first_name = firstname
        user.email = email
        user.username = username
        user.set_password(password)
        user.save()

        prof = Prof()
        prof.bio = bio
        prof.photo = photo
        prof.mat_ens = form
        prof.save()
        return render(request, 'accounts/register_prof.html')
    else:
        context = {
            'matiere': matiere,
        }
        return render(request, 'accounts/register_prof.html', context)


# **********************************************


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('home')


def upload(request):
    if request.method == 'POST':
        form = DocForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ged')

    else:
        form = DocForm()
    return render(request, 'ged/upload.html', {'form': form})


def delete_doc(request, pk):
    if request.method == 'POST':
        doc = Document.objects.get(pk=pk)
        doc.delete()
    return redirect('ged')


def ged(request):
    classes = Classe.objects.all()
    doc = Document.objects.all()
    eleve = Eleve.objects.get(eleve_user=request.user)
    matier = Matiere.objects.filter(id_classe=eleve.class_eleve)
    context = {
        'doc': doc,
        'matier': matier,
        'classes': classes

    }
    return render(request, 'ged/dashboard.html', context)
