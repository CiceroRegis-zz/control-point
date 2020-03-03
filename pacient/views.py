from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _
from django.views.decorators.http import require_GET

from pacient.form import PacientForm
from pacient.models import Pacient


@login_required
def registerPacient(request):
    form = PacientForm()
    if request.method == 'POST':
        form = PacientForm(request.POST, request.FILES)
    try:    
        if form.is_valid():
            form.save()
            form = PacientForm()
            messages.success(request, _("Pacient was successfully Saved!"))
            return redirect("pacient:pacient-list")
        else:
            context = {'form' : form}
            return render(request, 'pacient/pacient-register.html', context)
    except Exception:
        messages.warning(request, _('Error Form'))
        
        
@login_required
def updatePacient(request, pk):
    pacient = Pacient.objects.get(id=pk)
    if request.method == "POST":
        form = PacientForm(request.POST, instance=pacient)
        if form.is_valid():
            form.save()
            messages.success(request, _("Pacient was successfully updated!"))
            return redirect("pacient:pacient-list")
        else:
            messages.warning(request, _("Please correct the error below."))
    else:
        form = PacientForm(instance=pacient)
    
        context = {
            
            "form": form,
            }
    return render(request, "pacient/pacient-register.html", context)


@login_required
@require_GET
def pacientList(request):
    context = {'pacients' : Pacient.objects.all().order_by('name'),}
    return render(request, "pacient/pacient-list.html", context)


@login_required
@require_GET
def showDetails(request, pk):
    context = {'showDetails' : Pacient.objects.filter(id=pk)}
    return render(request, 'pacient/show-details.html', context)