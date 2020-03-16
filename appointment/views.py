from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import DecimalField, F, ExpressionWrapper, Sum, Count
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from django.views.decorators.http import require_GET

from appointment.admin import Appointment
from appointment.form import AppointmentForm
from appointment.models import Appointment, TypeAppointment


@login_required
def createAppointment(request):
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
@require_GET
def listAppointment(request):
    search = request.GET.get('search')
    if search:
        appointments = Appointment.objects.filter(pacient__name__icontains=search)
    else:
        appointments = Appointment.objects.all().order_by('date_appointment')
        appointments_total = TypeAppointment.objects.filter(
            appointment=F('price') + F('price')).values('price')
        paginator = Paginator(appointments, 6)
        page = request.GET.get('page', 1)
        try:
            appointments = paginator.get_page(page)
        except PageNotAnInteger:
            appointments = paginator.get_page(2)
        except EmptyPage:
            appointments = paginator.get_page(paginator.num_pages)
    context = {'appointments': appointments,
               'appointments_total': appointments_total
               }
    return render(request, "appointment/list-appointments.html", context)

# @login_required
# @require_GET
# def showValuesCardshome(request):
#     appointments = Appointment.objects.count()
#     context = {'appointments': appointments}
#     return render(request, "base/home-cards.html", context)
