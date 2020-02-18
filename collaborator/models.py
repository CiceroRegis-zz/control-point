from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Collaborator(models.Model):
    
    SEXO_CHOICES = (
        ('M', _('Masculino')),
        ('F', _('Feminino')),
    )
    
    user = models.OneToOneField(User,null=True, blank=True, on_delete=models.DO_NOTHING, verbose_name=_('User'))
    nome = models.CharField(max_length=100)
    birth = models.DateField(null=True, blank=True, verbose_name='date of birth')
    sexo = models.CharField(max_length=1, blank=True, null=True, choices=SEXO_CHOICES)
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name='phone number')
    isWhatsapp = models.BooleanField(default=False, verbose_name=_('Is whatsapp'),)
    cpf = models.CharField(max_length=15, blank=True, null=True, verbose_name='CPF')
    landline = models.CharField(max_length=15, blank=True, null=True, verbose_name='landline')
    updateAt = models.DateTimeField(null=False, blank=False, editable=False, auto_now=True)
    createAt = models.DateTimeField(null=False, blank=False, editable=False, auto_now_add=True)

    def __str__(self):
        return self.nome

    def birthday(self):
        _date = self.birth
        return _date.strftime('%d/%m/%Y')
