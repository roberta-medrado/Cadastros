from django.shortcuts import render
from CadastroCliente.models import Cliente, Profissao


# Create your views here.
def index(request):
    meu_nome = 'Beltrano da Costa'
    lista_frutas = ['Laranja', 'Maça', 'Banana']
    context = {
        'nome': meu_nome,
        'frutas': lista_frutas
        }
    return render(request, 'index.html', context)

def listar_clientes(request):
    # busca todos os clientes cadastrados na tabela (admin)
    lista_clientes = Cliente.objects.all()
    profissoes = Profissao.objects.all()
    # o dicionário (variável) context é que vai mandar para o template
    context = {
        "clientes": lista_clientes,
        "profissoes": profissoes        
    }
    return render(request, 'lista_clientes.html', context)

def listar_profissoes(request):
    profissoes = Profissao.objects.all()
    context = {
        "profissoes": profissoes
    }
    return render(request, 'profissoes.html', context)

def detalhar_cliente(request, id):
    # buscando no banco de dados o cliente pelo id
    cliente = Cliente.objects.get(id = id)
    context = {
        "cliente": cliente
    }
    return render(request, "cliente_detalhes.html", context)