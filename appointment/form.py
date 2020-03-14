from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from appointment.models import Appointment
from pacient.models import Pacient


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        exclude = (
            "updateAt",
            "createAt",
        )

    type_appointment = forms.MultipleChoiceField(
        error_messages={"required": _("type appointment is required")},
        widget=forms.SelectMultiple(
            attrs={
                "class": "form-control",
            }
        ),
    )

    pacients = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={"class": "form-control", "placeholder": "Paciente"}
        ),
        queryset=Pacient.objects.all()
    )

    professional = forms.ModelChoiceField(
        widget=forms.Select(attrs={"class": "form-control", "placeholder": "Profissional"}),
        queryset=User.objects.all()
    )

    date_appointment = forms.DateField(
        input_formats=["%d/%m/%Y"],
        error_messages={"required": _("date appointment is required")},
        widget=forms.DateInput(
            attrs={
                "class": "form-control datetimepicker",
                "autocomplete": "off",
                "id": "birth_date",
                "placeholder": "Data da consulta",
            }
        ),
    )
