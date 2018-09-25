from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from ._forms import UserRegistrationFrom


# Create your views here.
def get_login(request):
    template_name = 'accounts/login.html'
    if request.user.is_authenticated:
        return redirect('archive')
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            auth = authenticate(request, username=username, password=password)
            if auth is not None:
                login(request, auth)
                return redirect('archive')
            else:
                messages.error(request, 'Username or Password is not valid!')
    return render(request, template_name)


def get_register(request):
    template_name = 'accounts/registration.html'
    form = UserRegistrationFrom(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Registration successful.')
        return redirect('login')
    return render(request, template_name, {'form': form})


def get_logout(request):
    logout(request)
    return redirect('/')
