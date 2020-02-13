from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput
    )


class RegisterForm(forms.Form):

    username = forms.CharField(
        error_messages={'required': 'Obrigatório o preenchimento do Usuario de login'},
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Login'}),
    )

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

    def clean_username(self):
        username = self.cleaned_data['username']
        queryset = User.objects.filter(username=username)
        if queryset.exists():
            raise forms.ValidationError('Esse usuario já existe, escolha outro nome')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        queryset = User.objects.filter(email=email)
        if queryset.exists():
            raise forms.ValidationError('Esse email já existe, tente outro')
        return email

    def clean_confirm_password(self):
        data = self.cleaned_data 
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('As senhas informadas deve ser iguais')
        return data
