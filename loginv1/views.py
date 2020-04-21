from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import *
from django.contrib.auth.models import Group


# Create your views here.
def index(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            return redirect('authv1:loginv1')
    else:
        form = UserRegisterForm()

    context = {"form": form}

    return render(request, 'register.html', context)


@login_required
def profile(request):
    return render(request, 'profile.html')
