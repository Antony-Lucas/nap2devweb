from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.contrib import messages

User = get_user_model()
def index_view(request):
    return render(request, 'index.html')

def login_view(request):
    error_message = None
    login_form = LoginForm()
    register_form = CustomUserCreationForm()
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if 'login-form' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                
                return redirect('index') 
            else:
                error_message = "Usuário ou senha inválidos"
                print(error_message)
        elif 'register-form' in request.POST:
            register_form = CustomUserCreationForm(request.POST)
            if register_form.is_valid():
                register_form.save()
                return redirect('login')  
            else:
                print("Erros no formulário de registro:", register_form.errors)
                error_message = register_form.errors
    else:
        register_form = CustomUserCreationForm()

    context = {
        'login_form': login_form,
        'register_form': register_form,
        'show_register': False,
        'error_message': error_message,
        'is_authenticated': request.user.is_authenticated 
    }
    return render(request, 'auth/login.html', context)

def edit_perfil(request):
    return render(request, 'perfil_usuario/editar_perfil_usuario.html')

def encomenda(request):
    return render(request, 'perfil_usuario/encomendas.html')

def transport(request):
    return render(request, 'transport/transport.html')
