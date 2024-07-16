from .views import *

from django.urls import path
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('register',RegistrationView.as_view(),name ='registrador'),
    path('validate-username',csrf_exempt(UsernameValidationView.as_view()),name = 'validate-username')
]