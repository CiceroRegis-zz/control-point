from django.contrib import admin

from pacient.form import PacientForm
from pacient.models import Pacient

# Register your models here.

@admin.register(Pacient)
class PacientAdmin(admin.ModelAdmin):
    model = PacientForm
    list_display = ('name', 'medical_record_number', 'phone_number', 'landline', 'email', 'address', 'birthday', 'sexo')