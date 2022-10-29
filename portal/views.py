from asyncio.base_subprocess import BaseSubprocessTransport
import email
from pyexpat.errors import messages
from django.contrib import messages
from re import sub
from django.shortcuts import render, redirect
from portal.models import Categoria
from portal.models import Curso
from portal.models import Usuario
from portal.models import Aula
from portal.models import Matricula
from portal.forms import CategoriaForm
from portal.forms import CursoForm
from portal.forms import AulaForm
from portal.forms import MatriculaForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
import os

# Create your views here.

def home(request):
    return render(request, 'home.html')


@staff_member_required(login_url='/login')
def categoria(request):
    categorias = Categoria.objects.all()

    context = {
        'categorias' : categorias
    }
    return render(request, 'categoria.html', context)


@staff_member_required(login_url='/login')
def categoria_add(request):
    if request.method == 'GET':
        return render (request, 'categoria_add.html')
    else:
        nome_categoria = request.POST.get('nome_categoria')
        
        categoria = Categoria.objects.filter(nome_categoria=nome_categoria).first()
        if categoria:
            messages.info(request, 'Essa categoria já está cadastrada em nosso sistema!')
            return redirect('categoria_add')
        else:
            categoria = Categoria(nome_categoria = nome_categoria)
            categoria.save()
            messages.info(request, 'Categoria cadastrada com sucesso!')
            return redirect('categoria')


@staff_member_required(login_url='/login')
def categoria_edit(request,categoria_pk):
    categoria = Categoria.objects.get(pk=categoria_pk)

    form = CategoriaForm(request.POST or None, instance=categoria)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect ('categoria')

    context = {
        'categoria': categoria.id,
        'form': form,
    }

    return render(request, 'categoria_edit.html', context)


@staff_member_required(login_url='/login')
def categoria_delete(request,categoria_pk):
    categoria = Categoria.objects.get(pk=categoria_pk)
    categoria.delete()
    return redirect ('categoria')


@login_required(login_url='/login')
def cursos(request):
    cursos = Curso.objects.all()

    context = {
        'cursos' : cursos
    }
    return render(request, 'cursos.html', context)


@staff_member_required(login_url='/login')
def curso(request):
    cursos = Curso.objects.all()

    context = {
        'cursos' : cursos
    }
    return render(request, 'curso.html', context)


@staff_member_required(login_url='/login')
def curso_add(request):
    if request.method == 'GET':
        categorias = Categoria.objects.all()
        usuarios = Usuario.objects.all()
        context = {
            'categorias':categorias,
            'usuarios':usuarios
        }
        return render (request, 'curso_add.html',context)
    else:
        nome_curso = request.POST.get('nome_curso')
        usuario = request.POST.get('usuario')
        usuario = Usuario.objects.get(id=usuario)
        categoria = request.POST.get('categoria')
        categoria = Categoria.objects.get(id=categoria)
        descricao = request.POST.get('descricao')
        thumbnail = request.FILES.get('thumbnail')
        # video_url = request.POST.get('video_url')

        buscacurso = Curso.objects.filter(nome_curso=nome_curso).first()
        if buscacurso:
            messages.info(request, 'Esse curso já está cadastrado em nosso sistema')
            return redirect('curso_add')
        else:
            # curso = Curso(nome_curso=nome_curso, usuario=usuario, categoria=categoria, descricao=descricao, thumbnail=thumbnail, video_url=video_url)
            curso = Curso(nome_curso=nome_curso, usuario=usuario, categoria=categoria, descricao=descricao, thumbnail=thumbnail)
            curso.save()
            messages.info(request, 'Curso cadastrado com sucesso!')
            return redirect('curso')


@staff_member_required(login_url='/login')
def curso_edit(request,curso_pk):
    curso = Curso.objects.get(pk=curso_pk)

    form = CursoForm(request.POST or None, instance=curso)
    
    if request.POST:
        if form.is_valid():
            form = CursoForm(request.POST, request.FILES, instance=curso)
            # if curso.thumbnail.path != None:
                # if os.path.exists(curso.thumbnail.path):  # MELHORIA apagar a imagem anterior
                    # os.remove(curso.thumbnail.path)       # o problema é se for repetida
            form.save()
            return redirect ('curso')

    context = {
        'curso': curso.id,
        'form': form,
    }

    return render(request, 'curso_edit.html', context)


@staff_member_required(login_url='/login')
def curso_delete(request,curso_pk):
    curso = Curso.objects.get(pk=curso_pk)
    curso.delete()
    return redirect ('curso')


@staff_member_required(login_url='/login')
def aula(request):
    aulas = Aula.objects.all()

    context = {
        'aulas' : aulas
    }
    return render(request, 'aula.html', context)


@login_required(login_url='/login')
def matricula(request):
    matriculas = Matricula.objects.all()

    context = {
        'matriculas' : matriculas
    }
    return render(request, 'matricula.html', context)



@staff_member_required(login_url='/login')
def aula_add(request):
    if request.method == 'GET':
        cursos = Curso.objects.all()
        # usuarios = Usuario.objects.all()
        context = {
            'cursos':cursos,
            # 'usuarios':usuarios
        }
        return render (request, 'aula_add.html',context)
    else:
        curso = request.POST.get('curso')
        curso = Curso.objects.get(id=curso)
        nome_aula = request.POST.get('nome_aula')
        video_url = request.POST.get('video_url')

        buscaaula = Aula.objects.filter(nome_aula=nome_aula).first()
        if buscaaula:
            messages.info(request, 'Essa aula já está cadastrado em nosso sistema')
            return redirect('aula_add')
        else:
            aula = Aula(curso=curso, nome_aula=nome_aula, video_url=video_url)
            aula.save()
            messages.info(request, 'Aula cadastrada com sucesso!')
            return redirect('aula')


@login_required(login_url='/login')
def matricula_add(request):
    if request.method == 'GET':
        cursos = Curso.objects.all()
        # usuarios = Usuario.objects.all()
        context = {
            'cursos':cursos,
            # 'usuarios':usuarios
        }
        return render (request, 'matricula_add.html',context)
    else:
        curso = request.POST.get('curso')
        curso = Curso.objects.get(id=curso)
        usuario = request.user # precisei tirar o .id do user.id sei lá porque
        buscamatricula = Matricula.objects.filter(usuario=usuario, curso=curso).first()
        
        if buscamatricula:
            messages.info(request, 'Esse usuário já está matriculado nesse curso')
            return redirect('matricula_add')
        else:
            matricula = Matricula(curso=curso, usuario=usuario)
            matricula.save()
            messages.info(request, 'Matrícula realizada com sucesso!')
            return redirect('matricula')



@staff_member_required(login_url='/login')
def aula_edit(request,aula_pk):
    aula = Aula.objects.get(pk=aula_pk)

    form = AulaForm(request.POST or None, instance=aula)
    
    if request.POST:
        if form.is_valid():
            form = AulaForm(request.POST, request.FILES, instance=aula)
            form.save()
            return redirect ('aula')

    context = {
        'aula': aula.id,
        'form': form,
    }

    return render(request, 'aula_edit.html', context)


@staff_member_required(login_url='/login')
def aula_delete(request,aula_pk):
    aula = Aula.objects.get(pk=aula_pk)
    aula.delete()
    return redirect ('aula')


@login_required(login_url='/login')
def matricula_delete(request,matricula_pk):
    matricula = Matricula.objects.get(pk=matricula_pk)
    matricula.delete()
    return redirect ('matricula')


def cadastro(request):
    if request.method == 'GET':
        return render (request, 'cadastro.html')
    else:
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        count_nums = 0
        # checagem de caracteres
        for c in nome:
            if c.isdigit():
                count_nums += 1
        if count_nums > 0:
            messages.info(request, 'O nome deve conter apenas letras')
            return redirect('cadastro')
        if len(nome.strip()) == 0 or len(email.strip()) == 0 or len(username.strip()) == 0:
            messages.info(request, 'Favor inserir corretamente nos campos nome, email e usuário.')
            return redirect('cadastro')
        if len(senha) < 6 or len(senha) > 10:
            messages.info(request, 'Favor inserir senha com no mínimo 6 e no máximo 10 caracteres')
            return redirect('cadastro')
    # contadores
    count_alpha = 0
    count_nums = 0
    # checagem de caracteres
    for c in senha:
        if c.isalpha():
            count_alpha += 1
        elif c.isdigit():
            count_nums += 1
    if count_alpha == 0 or count_nums == 0:
        messages.info(request, 'A senha deve conter letras e números')
        return redirect('cadastro')
    user = Usuario.objects.filter(email=email).first()
    if user:
        messages.info(request, 'Esse email de usuário já está cadastrado em nosso sistemas!')
        return redirect('cadastro')
    else:
        user = Usuario.objects.filter(username=username).first()
        if user:
            messages.info(request, 'Já existe um usuário com esse username!')
            return redirect('cadastro') 
        else:
            user = Usuario.objects.create_user(first_name = nome, last_name = sobrenome, email = email, username = username, password = senha)
            user.save()
            messages.info(request, 'Usuário cadastrado com sucesso!')
            return redirect('home')
                

def login(request):
    if request.method == 'GET':
        return render (request, 'login.html')
    else:
        username = request.POST.get('usuario')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)
        if user:
            login_django(request, user)
            return render(request, 'home.html')
        else:
            messages.info(request, 'Usuário ou senha inválidos!')
            return redirect('login')
        

def logout(request):
    logout_django(request)
    return render(request, 'home.html')
    
 