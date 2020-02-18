from django.contrib import admin

from collaborator.form import CollaboratorForm

# Register your models here.
from .models import Collaborator


@admin.register(Collaborator)
class CollaboratorAdmin(admin.ModelAdmin):
    form = CollaboratorForm
    list_display = ('nome', 'user', 'sexo', 'birthday')

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(CollaboratorAdmin, self).save_model(request, obj, form, change)
