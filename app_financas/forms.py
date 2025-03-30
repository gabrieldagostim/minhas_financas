from django import forms
from .models import Transacao


class TransacaoForm(forms.ModelForm):
    class Meta:
        model = Transacao
        fields = ['descricao','valor','categoria']
        labels = {
            'descricao': 'Descrição',
            'valor': 'Valor',
            'categoria': 'Categoria'
        }