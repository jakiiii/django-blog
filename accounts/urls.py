from django.urls import path

from . views import (
    LoginView,
    RegisterView,
    get_logout,
)


urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('registration/', RegisterView.as_view(), name='registration'),
    path('logout/', get_logout, name='logout')
]
