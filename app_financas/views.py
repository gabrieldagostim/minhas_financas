from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Usuario, Categoria, Transacao # importanto a tabela
from .forms import TransacaoForm # o ponto é porque ta no mesmo arquivo
from django.urls import reverse
# Create your views here.

# aqui a gente vai criar a lógica atraves do site

# podemos definir as funções ou classes, pra usar aqui
# ex:. quando o usuário entrar no link de finanças, verificar se ele está logado
# caso ele não estiver jogar pra login .... etc
# (aqui vai ser o backend)

def index(request):
    '''Pagina principal das minhas finanças'''
    return render(request, 'index.html')


def home(request):
    if request.method == "GET":
        return render(request, 'home.html')
    else:
        nome = request.POST.get('nome')
        # return HttpResponse('Formulário enviado! %s ' % nome)
    
        user = Usuario(
            nome = nome
        )

        user.save()
    
        return HttpResponse(f'Formulário enviado! {nome}')
    

def transacoes(request):
    '''Mostra todas as transacoes registrada'''
    if request.method == 'GET':
        transacoes = Transacao.objects.order_by('data_transacao')
        context = {'transacoes': transacoes} # para retornar o contexto

        return render(request, 'transacoes.html', context=context)
    

def cadastro_transacoes(request):
    '''Adciona uma nova transação financeira.'''

    if request.method != 'POST':
        # Nenhum dado submetido
        form = TransacaoForm()  

    else:
        # Dados de POST submetidos, processa os dadas
        form = TransacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('transacoes'))
        
    context = {'form': form}
    return render(request, 'nova_transacao.html', context)


def transacoes_por_cat(request, categoria_id):
    '''Mostra as transações dentro de cada categoria'''
    
    categoria = Categoria.objects.get(id = categoria_id)
    transacoes = categoria.transacao_set.order_by('-data_criado_em')
    context = {'categoria': categoria, 'transacoes': transacoes}

    return render(request, 'transacoes_por_categora.html',context=context)


def categorias(request):
    '''lista todas as categorias'''

    categorias = Categoria.objects.all().order_by('data_criado_em')
    context = {'categorias': categorias}

    return render(request, 'categorias.html', context=context)



def nova_categoria(request):
    return render(request, 'nova_categoria.html')

def processa_formulario(request):

    nome = request.POST.get('nome')
    email = request.POST.get('email')
    return HttpResponse(f' {nome} -> {email}')
