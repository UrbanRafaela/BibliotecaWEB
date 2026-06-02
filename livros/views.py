from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro
from .forms import LivroForm

@login_required
def lista_livros(request):
    pesquisa = request.GET.get('pesquisa')

    if pesquisa:
        livros = Livro.objects.filter(titulo__icontains=pesquisa)
    else:
        livros = Livro.objects.all()

    return render(request, 'livros/lista.html', {'livros': livros})

@login_required
def criar_livro(request):
    form = LivroForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('lista_livros')

    return render(request, 'livros/form.html', {'form': form})

@login_required
def editar_livro(request, id):
    livro = get_object_or_404(Livro, id=id)
    form = LivroForm(request.POST or None, request.FILES or None, instance=livro)
    if form.is_valid():
        form.save()
        return redirect('lista_livros')

    return render(request, 'livros/form.html', {'form': form})

@login_required
def excluir_livro(request, id):
    livro = get_object_or_404(Livro, id=id)

    if request.method == 'POST':
        livro.delete()
        return redirect('lista_livros')

    return render(request, 'livros/excluir.html', {'livro': livro})