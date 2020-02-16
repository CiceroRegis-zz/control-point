import time

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView

from collaborator.form import CollaboratorForm
from collaborator.models import Collaborator
from .forms import LoginForm, RegisterForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


def logout_page(request):
    context = {"content": "Você efetuou o logout com sucesso!"}
    logout(request)
    return render(request, "auth/login.html", context)


User = get_user_model()


@login_required
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form,
    }

    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data["username"]
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
        messages.success(request, _("Usuario salvo com sucesso"))
        context = {"form": RegisterForm()}

    return render(request, "auth/register.html", context)


@method_decorator(login_required, name="dispatch")
class CreatecollaboratorView(CreateView):
    model = Collaborator
    form_class = CollaboratorForm
    template_name = "register/register_collaborator.html"
    success_url = reverse_lazy("register_collaborator")

    def form_valid(self, form):
        super(CreatecollaboratorView, self).form_valid(form)
        # Add action to valid form phase
        collaborator = form.save(commit=False)
        if collaborator is None:
            username = collaborator.user.split('')[0] + collaborator.user.split('')[1]
            collaborator.user = User.objects.create(username=username)
            collaborator.save()
            messages.success(self.request, "Seus dados foram salvos com sucesso!")
        return HttpResponseRedirect(self.get_success_url())

    def get_form_kwargs(self):
        kwargs = super(CreatecollaboratorView, self).get_form_kwargs()
        kwargs.update({'username': self.request.user})
        return kwargs

    # def form_invalid(self, form):
    #     # Add action to invalid form phase
    #     super(CreatecollaboratorView, self).form_invalid(form)
    #     # Add action to valid form phase
    #     messages.warning(self.request, 'Ocorreu um erro ao tentar salvar dos dados!')
    #     return self.render_to_response(self.get_context_data(form=form))


class ListCollaborator(ListView):
    model = Collaborator
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def showProfile(request):
    context = {
        'profile': Collaborator.objects.filter(user=request.user)
    }
    return render(request, 'collaborator/profile_collaborator.html', context)
