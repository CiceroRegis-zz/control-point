from django import forms

from collaborator.models import Collaborator


class CollaboratorForm(forms.ModelForm):
    nome = forms.CharField(
        error_messages={'required': 'Obrigatório o preenchimento do nome'},
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo'}),
    )
    birth = forms.CharField(
        error_messages={'required': 'Obrigatório o preenchimento da data de nascimento'},
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Data de nascimento'}),
    )

    class Meta:
        model = Collaborator
        exclude = ('updateAt', 'createAt',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].widget.attrs.update({'placeholder': 'Username', 'class': 'form-control'})
