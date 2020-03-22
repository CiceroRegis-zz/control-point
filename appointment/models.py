from datetime import datetime
from django.utils import timezone
from django.db import models
from django.db.models import Sum
from django.utils.translation import gettext_lazy as _

from collaborator.models import Profile
from pacient.models import Pacient


class TypeAppointment(models.Model):
    class Meta:
        db_table = "typeAppointment"
        verbose_name = _("typeAppointment")
        verbose_name_plural = _("typeAppointment")

    name = models.CharField(max_length=200, verbose_name=_('Name'))
    skip = models.BooleanField(default=False, verbose_name=_('Skip'))
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_('Price of appointment'))
    updateAt = models.DateTimeField(null=False, blank=False, editable=False, auto_now=True)
    createAt = models.DateTimeField(null=False, blank=False, editable=False, auto_now_add=True)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    class Meta:
        db_table = "appointment"
        verbose_name = _("appointment")
        verbose_name_plural = _("appointment")

    type_appointment = models.ManyToManyField(TypeAppointment,
                                              verbose_name=_('Type appointment'))
    pacient = models.ForeignKey(Pacient, on_delete=models.PROTECT, verbose_name=_('Pacient'))
    professional = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, verbose_name=_('Professional'))
    date_appointment = models.DateTimeField(verbose_name=_('date of appointment'))
    consulting = models.BooleanField(default=False, verbose_name=_('Consulting'))
    updateAt = models.DateTimeField(null=False, blank=False, editable=False, auto_now=True)
    createAt = models.DateTimeField(null=False, blank=False, editable=False, auto_now_add=True)

    @property
    def date_now(self):
        now = timezone.now()
        return now < self.date_appointment

    # def get_type_appointment(self):
    #     return "\n".join([p.name for p in self.type_appointment.all()])
