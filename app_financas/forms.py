from django import forms
from .models import Transacao


class TransacaoForm(forms.ModelForm):
    class Meta:
        model = Transacao
        fields = ['data_transacao','descricao','valor','categoria']
        labels = {
            'data_transacao':'Data Transação',
            'descricao': 'Descrição',
            'valor': 'Valor',
            'categoria': 'Categoria'
        }