from django.shortcuts import redirect
from django.views.generic import CreateView, FormView
from django.contrib.messages.views import SuccessMessageMixin, messages
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm, RegistrationForm


# Create your views here.
class LoginView(FormView):
    form_class = LoginForm
    success_url = '/archive/'
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, email=email, password=password)

        if user is not None:
            login(self.request, user)
        else:
            messages.error(self.request, 'Username or Password is not valid!')
            return redirect('login')
        return super(LoginView, self).form_valid(form)


class RegisterView(SuccessMessageMixin, CreateView):
    form_class = RegistrationForm
    template_name = 'accounts/registration.html'
    success_message = 'Registration successful.'
    success_url = '/accounts/'


def get_logout(request):
    logout(request)
    return redirect('/')
