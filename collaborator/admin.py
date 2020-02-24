from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from collaborator.form import CollaboratorForm
from collaborator.models import User

# Register your models here.
from .models import Collaborator

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

class CollaboratorInline(admin.StackedInline):
    model = Collaborator
    can_delete = True
    verbose_name_plural = 'Collaborator'
    fk_name = 'user'
    
class CustomUserAdmin(UserAdmin):
    inlines = (CollaboratorInline, )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'nome')
    list_select_related = ('collaborator', )

    

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)
    
       

@admin.register(Collaborator)
class CollaboratorAdmin(admin.ModelAdmin):
    form = CollaboratorForm
    list_display = ('nome', 'user', 'sexo','phone_number', 'isWhatsapp', 'landline', 'birth_date', 'createAt')
    readonly_fields = ['cpf']
