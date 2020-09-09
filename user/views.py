from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def user(request):
    return redirect('login')

def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
        'form' : form,
    }
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username = username, password = password)
        if user is None:
            messages.info(request, 'Kullanıcı bulunamadı')
            return render(request, 'login.html', context)
        messages.success(request, 'Giriş başarılı')
        login(request, user)
        return redirect('index')
    return render(request, "login.html", context)

@login_required(login_url="user:login") 
def logoutUser(request):
    logout(request)
    messages.success(request, 'Çıkış başarılı')
    return redirect('index')