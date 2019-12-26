from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User

from .models import Collaborator


@admin.register(Collaborator)
class CollaboratorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'user', 'birthday')

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(Collaborator.user, self).save_model(request, obj, form, change)
