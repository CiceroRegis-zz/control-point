from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta:
        db_table = 'User'
        verbose_name = _('User')


class Collaborator(models.Model):
    
    class Meta:
        db_table = 'Collaborator'
        verbose_name = _('Collaborator')
    
    SEXO_CHOICES = (
        ('M', _('Masculino')),
        ('F', _('Feminino')),
    )
    
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('User'))
    nome = models.CharField(max_length=100)
    birth = models.DateField(null=True, blank=True, verbose_name='date of birth')
    sexo = models.CharField(max_length=1, default='', blank=False, null=False, choices=SEXO_CHOICES)
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
