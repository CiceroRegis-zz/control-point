from django.contrib import admin

# Register your models here.
from .models import Collaborator


@admin.register(Collaborator)
class CollaboratorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'user', 'birthday')

    def save_model(self, request, obj, form, change):
        obj.user = request.user
