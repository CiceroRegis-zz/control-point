import time

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model, logout
from .forms import LoginForm, RegisterForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


def logout_page(request):
    context = {
        'content': 'Você efetuou o logout com sucesso!'
    }
    logout(request)
    return render(request, 'auth/login.html', context)


User = get_user_model()

@login_required
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form,
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
        messages.success(request, _('Usuario salvo com sucesso'))
        context = {
            'form': RegisterForm()
        }

    return render(request, 'auth/register.html', context)
