from django.shortcuts import render

# Create your views here.

def index(request):

    nome_usuario = 'Estudante IFRN'

    contexto = {

        'nome_usuario' : nome_usuario,

    }

    return render(request, 'ifrn/usuario.html', contexto)


def disciplinas(request):

    disciplinas = ["Django", "Python", "HTML", "Matemática", "Física", 'Química']

    contexto = {

        'disciplinas' : disciplinas,
    }

    return render(request, 'ifrn/disciplinas.html', contexto)


def autorizacao(request):

    valor_Boler = True

    contexto = {

        'valor_Boler': valor_Boler,

    }

    return render(request, 'ifrn/autorizacao.html', contexto)


def livraria(request):

    livro = {
        'titulo' : 'Memórias Póstumas de Brás Cubas',
        'autor' : 'Joaquim Machado de Assis',
        'ano' : 1881,
    }

    contexto = {

        'livro' : livro
    }

    return render(request, 'ifrn/livros.html', contexto)


def melhordisciplinas(request):

    disciplinas = []

    contexto = {

        'disciplinas' : disciplinas,
    }

    return render(request, 'ifrn/discimelhoradas.html', contexto)


def nivel(request):

    nivel_prioridade = 1

    contexto = {
        'nivel_prioridade' : nivel_prioridade,
    }

    return render(request, 'ifrn/nivel.html', contexto)


def lista(request):

    alunos = [
        {'nome': 'Francisca Thayane', 'matricula': '20231094010005'},
        {'nome': 'Francisco Guilherme', 'matricula': '20231094010089'},
        {'nome': 'Anna Angelina', 'matricula': '20231094010047'},
        {'nome': 'Leticia Maria', 'matricula': '20231094010025'},
    ]

    contexto = {

        'alunos' : alunos,
    }

    return render(request, 'ifrn/alunos.html', contexto)


def ordemlista(request):

    alunos = [
        {'nome': 'Francisca Thayane', 'matricula': '20231094010005'},
        {'nome': 'Francisco Guilherme', 'matricula': '20231094010089'},
        {'nome': 'Anna Angelina', 'matricula': '20231094010047'},
        {'nome': 'Leticia Maria', 'matricula': '20231094010025'},
    ]

    contexto = {

        'alunos' : alunos,
    }

    return render(request, 'ifrn/ordemalunos.html', contexto)


def idlista(request):

    alunos = [
        {'id': 1, 'nome': 'Francisca Thayane', 'matricula': '20231094010005'},
        {'id': 2, 'nome': 'Francisco Guilherme', 'matricula': '20231094010089'},
        {'id': 3, 'nome': 'Anna Angelina', 'matricula': '20231094010047'},
        {'id': 4, 'nome': 'Leticia Maria', 'matricula': '20231094010025'},
    ]

    contexto = {

        'alunos' : alunos,
    }

    return render(request, 'ifrn/modernoaluno.html', contexto)

def detalhes(request, id):
    return render(request, 'ifrn/detalhes.html', {'id': id})


def alerta(request):

    mostrar_alerta = True

    contexto = {
        'mostrar_alerta': mostrar_alerta
    }

    return render(request, 'ifrn/alerta.html', contexto)