from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth import get_user_model, logout, authenticate, login
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Encomenda
from .forms import CustomUserForm, EncomendaForm

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

@login_required
def edit_perfil(request):
    user = request.user 

    if request.method == 'POST':
        form = CustomUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return render(request, 'perfil_usuario/editar_perfil_usuario.html', {'form': form, 'success': True})
    else:
        form = CustomUserForm(instance=user)

    return render(request, 'perfil_usuario/editar_perfil_usuario.html', {'form': form})


@login_required
def cadastrar_encomenda(request):
    if request.method == 'POST':
        form = EncomendaForm(request.POST)
        if form.is_valid():
            encomenda = form.save(commit=False)
            encomenda.usuario = request.user 
            encomenda.save()
            return redirect('encomenda')  
    else:
        form = EncomendaForm()
    return render(request, 'transport/transport.html', {'form': form})

@login_required
def editar_encomenda(request, pk):
    encomenda = get_object_or_404(Encomenda, pk=pk, usuario=request.user)
    if request.method == 'POST':
        form = EncomendaForm(request.POST, instance=encomenda)
        if form.is_valid():
            form.save()
            return redirect('listar_encomendas') 
    else:
        form = EncomendaForm(instance=encomenda)
    return render(request, 'transport/trasnport.html', {'form': form})

@login_required
def excluir_encomenda(request, pk):
    encomenda = get_object_or_404(Encomenda, pk=pk, usuario=request.user)
    encomenda.delete()
    return redirect('listar_encomendas')  

@login_required
def listar_encomendas(request):
    encomendas = Encomenda.objects.filter(usuario=request.user)
    return render(request, 'perfil_usuario/encomendas.html', {'encomendas': encomendas})

def transport(request):
    return render(request, 'transport/transport.html')

def encomenda(request):
    return render(request, "perfil_usuario/encomendas.html")

def logout_view(request):
    logout(request)
    return render(request, 'index.html')