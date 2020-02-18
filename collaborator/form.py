from django import forms
from django.utils.translation import gettext_lazy as _

from collaborator.models import Collaborator
from django.contrib.auth.models import User


class CollaboratorForm(forms.ModelForm):
    nome = forms.CharField(
        error_messages={"required": "Obrigatório o preenchimento do nome"},
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Nome completo"}
        ),
    )
    birth = forms.DateTimeField(
        input_formats=["%d/%m/%Y"],
        error_messages={
            "required": "Obrigatório o preenchimento da data de nascimento"
        },
        widget=forms.TextInput(
            attrs={
                "class": "form-control datepicker",
                "autocomplete": "off",
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

    def clean_cpf(self):
        cpf = self.cleaned_data["cpf"]
        queryset = Collaborator.objects.filter(cpf=cpf)
        if queryset.exists():
            raise forms.ValidationError("Já exite um usuário com este cpf")
        return cpf

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
    isWhatsapp = forms.BooleanField(
        error_messages={"required": "Este numero é whatsapp?"}, required=False
    )

    landline = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "landline",
                "placeholder": "Telefone Fixo",
            }
        ),
    )

    SEXO_CHOICES = (
        ("M", "Masculino"),
        ("F", "Feminino"),
    )

    sexo = forms.ChoiceField(
        choices=SEXO_CHOICES,
        widget=forms.Select(
            attrs={"class": "form-control", "placeholder": "Telefone Fixo"}
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
