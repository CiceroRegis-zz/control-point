import time

from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, ListView, UpdateView
from django.views.decorators.http import require_GET
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters

from collaborator.form import CollaboratorForm
from collaborator.models import Collaborator, User


@login_required
def logout_view(request):
    logout(request)
    return redirect("collaborator:logout")

@login_required
def registerCollaborator(request):
    form = CollaboratorForm()
    if request.method == "POST":
        form = CollaboratorForm(request.POST)
        if form.is_valid():
            form.save()
            form = CollaboratorForm()
            messages.success(request, _("Usuario cadastrado com sucesso"))
        else:
            messages.warning(
                request,_("Não foi possivel salvar os dados. Verifique se os campos estão correto!"),
            )
    context = {"form": form}
    return render(request, "register/register_collaborator.html", context)


@login_required
@require_GET
def listCollaborators(request):
    context = {"collaborators": Collaborator.objects.all().order_by("nome")}
    return render(request, "collaborator/collaborator_list.html", context)



@login_required
def updateProfileCollaborator(request, pk):
    collaborator = Collaborator.objects.get(id=pk)
    form = CollaboratorForm(instance=collaborator)
    
    if request.method == 'POST':
        form = CollaboratorForm(request.POST, instance=request.user.collaborator)
        if form.is_valid():
                form.save()
                messages.success(request, _("Usuario atualizado com sucesso"))
                return redirect("collaborator:list-collaborator")
        else:
            messages.warning(request, _("Por favor corrija o erro abaixo."))
        
    context = {"form": form}
    return render(request, "register/register_collaborator.html", context)


@login_required
@require_GET
def disableProfileCollaborator(request, collaborator):
    c = Collaborator.objects.get(pk=collaborator)
    if not c:
        messages.warning(request, _("This Collaborator not found."))
    try:
        if c:
            c.delete()
            messages.success(request, _("Collaborator canceled."))
    except Exception:
        messages.warning(request, _("Collaborator not canceled."))

    return redirect("collaborator:list-collaborator")


@login_required
@require_GET
def showProfile(request):
    context = {"profile": User.objects.filter(username=request.user)}
    return render(request, "collaborator/profile_user.html", context)


@login_required
def date_joined(request):
    context = {"date_joined": request.user.date_joined}
    date_joined.timedelta(days=3)
    return render(request, "collaborator/profile_collaborator.html", context)
