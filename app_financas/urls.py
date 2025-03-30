"""
URL configuration for minhas_financas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
""" 
from django.urls import path
from . import views

# include ->

urlpatterns = [
    path('', views.index, name='index'),
    path('transacoes', views.transacoes, name='transacoes'),
    path('cadastrar_transacao', views.cadastro_transacoes, name='nova_transacao'),
    path('transacoes_categorias/<categoria_id>', views.transacoes_por_cat, name='transacao_por_cat'), # Mostrar transações por cat
    path('categorias', views.categorias, name='categorias') # Mostrar transações por cat
]
