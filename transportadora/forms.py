from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password
from .models import CustomUser, Encomenda

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, required=True, help_text='Nome completo')

    class Meta:
        model = User
        fields = ('username', 'full_name', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'full_name', 'email', 'password', 'date_of_birth', 'contact', 'cpf', 
            'address', 'complement', 'city', 'zip_code'
        ]
        labels = {
            'full_name': 'Nome completo',
            'email': 'Email',
            'password': 'Senha',
            'date_of_birth': 'Data de nascimento',
            'contact': 'Contato',
            'cpf': 'CPF',
            'address': 'Endereço',
            'complement': 'Complemento',
            'city': 'Cidade',
            'zip_code': 'CEP',
        }
        widgets = {
            'password': forms.PasswordInput(),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')

        if password:
            user.password = make_password(password)
        else:
            user.password = self.instance.password 

        if commit:
            user.save()
        return user
    
class EncomendaForm(forms.ModelForm):
    class Meta:
        model = Encomenda
        fields = ['remetente', 'destinatario', 'etiqueta', 'cpf_destinatario', 'endereco_saida', 'endereco_destino']