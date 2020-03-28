import logging

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from django.views.decorators.http import require_GET

from appointment.admin import Appointment
from appointment.form import AppointmentForm, FilterForm
from appointment.models import Appointment

logger = logging.getLogger("django")


@login_required
def create_appointment(request):
    form = AppointmentForm()
    if request.method == "POST":
        form = AppointmentForm(request.POST)
    try:
        if form.is_valid():
            form.save()
            messages.success(request, _("Appointment was successfully created!"))
            return redirect("appointments:list-appointments")
        else:
            context = {"form": form}
            return render(request, "appointment/create-appointments.html", context)
    except Exception:
        messages.warning(request, _("Error Form"))


@require_GET
def show_total_values(request):
    appointments = Appointment.objects.all()
    return appointments


# @require_GET
# @login_required
# def show_total_values(request):
#     total_values = Appointment.objects.all().count()
#     context = {'show_total_values': total_values}
#     return render(request, 'appointment/home-cards.html', context)


@login_required
def list_appointment(request):
    form_filter = {}
    search = request.GET.get("search")

    date_appointment = FilterForm(request.GET)
    if date_appointment.is_valid():
        form_filter = date_appointment.cleaned_data

    if form_filter.get("date_appointment"):
        appointments = Appointment.objects.filter(
            date_appointment__gte=form_filter.get("date_appointment")
        )
    if search:
        appointments = Appointment.objects.filter(
            pacient__name__icontains=search
        ).annotate(total=Sum("type_appointment__price"))
    else:
        appointments = (
            Appointment.objects.all()
            .annotate(total=Sum("type_appointment__price"))
            .order_by("date_appointment")
        )

        paginator = Paginator(appointments, 5)
        page = request.GET.get("page", 1)
        try:
            appointments = paginator.get_page(page)
        except PageNotAnInteger:
            appointments = paginator.get_page(2)
        except EmptyPage:
            appointments = paginator.get_page(paginator.num_pages)
    context = {
        "appointments": appointments,
        "show_total_values": show_total_values(request),
    }
    return render(request, "appointment/list-appointments.html", context)


@login_required
def update_appointment(request, pk):
    appointment = Appointment.objects.get(id=pk)
    if request.method == "POST":
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                _(
                    "Appointment of "
                    + str(appointment.pacient)
                    + " was successfully updated!"
                ),
            )
            return redirect("appointments:list-appointments")
        else:
            messages.warning(request, _("Please correct the error below."))
    else:
        form = AppointmentForm(instance=appointment)
        context = {"form": form}
        return render(request, "appointment/create-appointments.html", context)


@require_GET
@login_required
def start_consultation(request, pk):
    a = Appointment.objects.get(id=pk)

    if not a.consulting:
        a.consulting = True
        a.save()
        messages.success(
            request, _("The consultation with the " + str(a.pacient) + " has started")
        )
    else:
        a.consulting = False
        a.save()
        messages.success(
            request, _("The consultation with the " + str(a.pacient) + " was canceled")
        )
    return redirect("appointments:list-appointments")
