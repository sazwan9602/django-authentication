from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .decorators import *
from django.contrib.auth.models import Group


# Create your views here.
def indexView(request):
    return render(request, 'index.html')


@login_required
@allowed_user(allowed_roles=['admin'])
def dashboardView(request):
    return render(request, 'dashboard.html')


@unauthenticated_user
def registerView(request):

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='admin')
            user.groups.add(group)

            messages.success(request, "Account created for " + username)
            return redirect('login_url')
    context = {"form": form}
    return render(request, 'registration/register.html', context)


@unauthenticated_user
def login_url(request):
    if request.POST:
        uname = request.POST.get('username')
        pword = request.POST.get('password')

        user = authenticate(request, username=uname, password=pword)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, "Username OR Password are incorrect")
    context = {}

    return render(request, 'registration/login.html', context)


def logout_url(request):
    logout(request)
    return redirect('login_url')
