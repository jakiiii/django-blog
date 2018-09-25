from django.urls import path

from . _views import (
    get_login,
    get_register,
    get_logout,
)


urlpatterns = [
    path('', get_login, name='login'),
    path('registration/', get_register, name='registration'),
    path('logout/', get_logout, name='logout')
]