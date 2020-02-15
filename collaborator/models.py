from django.contrib.auth.models import User
from django.db import models


class Collaborator(models.Model):
    nome = models.CharField(max_length=100)
    birth = models.DateField(null=True, blank=True)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.PROTECT)
    updateAt = models.DateTimeField(null=False, blank=False, editable=False, auto_now=True)
    createAt = models.DateTimeField(null=False, blank=False, editable=False, auto_now_add=True)

    def __str__(self):
        return self.nome

    def birthday(self):
        _date = self.birth
        return _date.strftime('%d/%m/%Y')

    
