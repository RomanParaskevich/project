from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserRegistration


# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Авторизация успешна')
                else:
                    return HttpResponse('Аккаунт отключен')
            else:
                return HttpResponse('Неправильный логин или пароль')
    else:
        form = LoginForm()
    return render(request, 'login.html',{'form': form})


def user_register(request):
    if request.method == 'POST':
        user_form = UserRegistration(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistration()
    return render(request, 'register.html', {'user_form': user_form})


def logout_view(request):
    logout(request)
    return HttpResponse('Вы вышли из учетной записи')
