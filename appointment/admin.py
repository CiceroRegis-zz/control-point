from django.contrib import admin

# Register your models here.
from appointment.models import Appointment, TypeAppointment


@admin.register(TypeAppointment)
class TypeAppointment(admin.ModelAdmin):
    model = TypeAppointment
    list_display = ('name', 'skip', 'price')


@admin.register(Appointment)
class Appointment(admin.ModelAdmin):
    model = Appointment
    list_display = ('pacient', 'professional')
    # readonly_fields = ('pacient', 'professional','type_appointment', 'createAt')
    filter_horizontal = ['type_appointment']