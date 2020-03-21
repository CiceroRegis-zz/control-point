from datetime import datetime

from django.contrib import messages
import logging
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from django.views.decorators.http import require_GET

from appointment.admin import Appointment
from appointment.form import AppointmentForm
from appointment.models import Appointment

logger = logging.getLogger('django')


@login_required
def create_appointment(request):
    form = AppointmentForm()
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
    try:
        if form.is_valid():
            form.save()
            messages.success(request, _("Appointment was successfully created!"))
            return redirect("appointments:list-appointments")
        else:
            context = {
                'form': form
            }
            return render(request, 'appointment/create-appointments.html', context)
    except Exception:
        messages.warning(request, _('Error Form'))


@login_required
def list_appointment(request):
    search = request.GET.get('search')
    if search:
        appointments = Appointment.objects.filter(pacient__name__icontains=search).annotate(
            total=Sum('type_appointment__price'))
    else:
        appointments = Appointment.objects.all().annotate(
            total=Sum('type_appointment__price')).order_by(
            'date_appointment')

        paginator = Paginator(appointments, 2)
        page = request.GET.get('page', 1)
        try:
            appointments = paginator.get_page(page)
        except PageNotAnInteger:
            appointments = paginator.get_page(2)
        except EmptyPage:
            appointments = paginator.get_page(paginator.num_pages)
    context = {'appointments': appointments}
    return render(request, "appointment/list-appointments.html", context)

# @login_required
# @require_GET
# def showValuesCardshome(request):
#     appointments = Appointment.objects.count()
#     context = {'appointments': appointments}
#     return render(request, "base/home-cards.html", context)
