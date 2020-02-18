from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from collaborator.form import CollaboratorForm
from collaborator.models import User

# Register your models here.
from .models import Collaborator

admin.site.register(User, UserAdmin)

@admin.register(Collaborator)
class CollaboratorAdmin(admin.ModelAdmin):
    form = CollaboratorForm
    list_display = ('nome', 'user', 'sexo','phone_number', 'isWhatsapp', 'landline', 'birthday', 'createAt')
    readonly_fields = [
        'cpf','birth'
    ]

