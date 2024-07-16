from django.shortcuts import render
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
# Create your views here.
class RegistrationView(View):
    def get(self, request):
        return render(request,'authentication/register.html')
    
class UsernameValidationView(View):
    def post(self,request):
        data = json.loads(request.body)
        username = data['username']

        if not str(username).isalnum():
            return JsonResponse({'username_error': 'usuário deve ter apenas caracteres alfanuméricos(1-9,a-z)'},status = 400)
        if User.objects.filter(username= username).exists():
            return JsonResponse({'username_error':'usuário já existe'})
        if User.objects.filter(username= username).exists:
            pass
        
        return JsonResponse({'username_valid':True})