from django import forms
from django.utils.translation import gettext_lazy as _

from collaborator.models import Collaborator
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput
    )

class CollaboratorForm(forms.ModelForm):
    
    nome = forms.CharField(
        error_messages={"required": "Obrigatório o preenchimento do nome"},
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Nome completo"}
        ),
    )
    
    user = forms.TextInput()

    email = forms.EmailField(
        error_messages={'required': 'Obrigatório o preenchimento do E-mail'},
        widget=forms.TextInput(
            attrs={'class': 'form-control validate', 'placeholder': 'E-mail', 'type': 'email'}),
    )

    password = forms.CharField(
        error_messages={'required': 'Senha obrigatoria'},
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha'}),
    )
    confirm_password = forms.CharField(
        error_messages={'required': 'Confirmar senha obrigatoria'},
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar Senha'}),
    )
    
    birth_date = forms.DateField(
        input_formats=["%d/%m/%Y"],
        error_messages={
            "required": "Obrigatório o preenchimento da data de nascimento"
        },
        widget=forms.DateInput(
            attrs={
                "class": "form-control",
                "autocomplete": "off",
                "id" : "birth_date",
                "placeholder": "Data de nascimento",
            }
        ),
    )

    cpf = forms.CharField(
        error_messages={"required": "Informe o cpf"},
        widget=forms.TextInput(
            attrs={"class": "form-control", "id": "CPF", "placeholder": "CPF"}
        ),
    )


    phone_number = forms.CharField(
        error_messages={"required": "Informe um numero de celular"},
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "phone_number",
                "placeholder": "Celular",
            }
        ),
    )
    isWhatsapp = forms.BooleanField(required=False)

    landline = forms.CharField(
        required=False,
        widget=forms.TextInput(
            
            attrs={
                "class": "form-control",
                "id": "landline",
                "placeholder": "Telefone Fixo",
            }
        ),
    )

    SEXO_CHOICES = (
        ('M', _('Masculino')),
        ('F', _('Feminino')),
    )

    sexo = forms.ChoiceField(
        choices=SEXO_CHOICES,required=True, label='Sexo',
        error_messages={"required": "Campo Sexo é obrigatório"},
        widget=forms.Select(
            attrs={"name": "select_0", "class": "form-control", "placeholder": "Telefone Fixo"}
        ),
    )

    class Meta:
        model = Collaborator
        exclude = (
            "updateAt",
            "createAt",
        )

    # def __init__(self, username, *args, **kwargs):
    #     super(CollaboratorForm, self).__init__(*args, **kwargs)
    # self.fields['user'].queryset = User.objects.filter(
    #    username=username)

    #     self.fields['user'].widget.attrs.update({'placeholder': 'Username', 'class': 'form-control'})
