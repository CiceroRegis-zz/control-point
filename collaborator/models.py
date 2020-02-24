from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.utils.timezone import localtime
from django.db.models.signals import post_save
from django.dispatch import receiver


class Collaborator(models.Model):
    
    class Meta:
        db_table = 'Collaborator'
        verbose_name = _('Collaborator')
    
    SEXO_CHOICES = (
        ('M', _('Masculino')),
        ('F', _('Feminino')),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('User'))
    nome = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True, verbose_name='birth date')
    sexo = models.CharField(max_length=1, default='', blank=False, null=False, choices=SEXO_CHOICES)
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name='phone number')
    isWhatsapp = models.BooleanField(default=False, verbose_name=_('Is whatsapp'),)
    cpf = models.CharField(max_length=15, blank=True, null=True, unique=True, verbose_name='CPF')
    landline = models.CharField(max_length=15, blank=True, null=True, verbose_name='landline')
    updateAt = models.DateTimeField(null=False, blank=False, editable=False, auto_now=True)
    createAt = models.DateTimeField(null=False, blank=False, editable=False, auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    
    @receiver(post_save, sender=User)
    def create_user_collaborator(sender, instance, created, **kwargs):
        if created:
            Collaborator.objects.create(user=instance)
        instance.collaborator.save()
        
    def birthday(self):
        _birth_date = self.birth_date.strftime('%d/%m/%Y')
        return _birth_date

