from django import forms

from collaborator.models import Collaborator
from django.contrib.auth.models import User


class CollaboratorForm(forms.ModelForm):
    nome = forms.CharField(
        error_messages={'required': 'Obrigatório o preenchimento do nome'},
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo'}),
    )
    birth = forms.DateTimeField(
        input_formats=['%d/%m/%Y'],
        error_messages={'required': 'Obrigatório o preenchimento da data de nascimento'},
        widget=forms.TextInput(
            attrs={'class': 'form-control datepicker', 'autocomplete': 'off',
                   'placeholder': 'Data de nascimento'}),
    )

    class Meta:
        model = Collaborator
        exclude = ('updateAt', 'createAt',)

    def __init__(self, username, *args, **kwargs):
        super(CollaboratorForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(
           username=username)
            
        self.fields['user'].widget.attrs.update({'placeholder': 'Username', 'class': 'form-control'})
