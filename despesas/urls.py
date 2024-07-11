from django.urls import path
from . import views



urlpatterns = [
    path("",views.index,name='despesas'),
    path('adicionar_despesa',views.adicionar_despesas,name="adicionar_despesas")
]