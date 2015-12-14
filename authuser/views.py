from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import  login as login_auth
from django.contrib.auth import logout as logout_auth
from django.contrib.auth.forms import AuthenticationForm # Formulario de autenticacao de usuarios
from django.contrib.auth import login,logout # funcao que salva o usuario na sessao

def home(request):
    return render(request, '../templates/home.html')

def registrar(request):

    # Se dados forem passados via POST
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid(): # se o formulario for valido
            form.save() # cria um novo usuario a partir dos dados enviados
            return HttpResponseRedirect("/login/") # redireciona para a tela de login
        else:
            # mostra novamente o formulario de cadastro com os erros do formulario atual
            return render(request, "cadastro.html", {"form": form})

    # se nenhuma informacao for passada, exibe a pagina de cadastro com o formulario
    return render(request, "cadastro.html", {"form": UserCreationForm() })

def login_req(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST) # Veja a documentacao desta funcao

        if form.is_valid():
            #se o formulario for valido significa que o Django conseguiu encontrar o usuario no banco de dados
            #agora, basta logar o usuario e ser feliz.
            login(request, form.get_user())
            #return redirect("../templates/home.html") # redireciona o usuario logado para a pagina inicial
            return render(request, '../templates/home.html')
        else:
            return render(request, "login.html", {"form": form})

    #se nenhuma informacao for passada, exibe a pagina de login com o formulario
    return render(request, "login.html", {"form": AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('home')
