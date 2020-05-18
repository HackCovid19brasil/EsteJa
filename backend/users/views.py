from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserForm
from .models import CustomUser

def signup(request):
    form_custom_user = CustomUserForm(request.POST, request.FILES)
    form_user = UserCreationForm(request.POST)
    mensagem = None
    if request.method == "POST":
        medico = form_custom_user
        user = form_user
        if user.is_valid():
            user = user.save(commit=False)
            if medico.is_valid():
                medico = medico.save(commit=False)
                user.is_active = False
                user.save()
                medico.user = user
                medico.save()
                mensagem = "Usuário cadastrado com sucesso. Aguarde a avaliação da administração."
                return render(request, 'index.html', {"mensagem": mensagem})
        else:
            mensagem = "Erro ao create_view usuário. Tente novamente."
            return render(request, 'users/create_view.html', {'form_user': form_user, 'form_custom_user': form_custom_user,"mensagem": mensagem})
    context = {
        'form_user': form_user,
        'form_custom_user': form_custom_user,
        'mensagem': mensagem
    }
    return render(request, 'users/create_view.html', context)

def list_view(request):
    users = User.objects.all()
    return render(request, 'users/list_view.html', {'users': users})

def perfil(request, id):
    user = get_object_or_404(User, id = id)
    custom_user = get_object_or_404(CustomUser, user=user)
    return render(request, 'users/perfil.html', {'custom_user': custom_user})

def delete_view(request, id):
    user = get_object_or_404(User, id = id)
    user.delete()
    return redirect('user:list_view')
