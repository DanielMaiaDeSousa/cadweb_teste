from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Categoria
from .forms import CategoriaForm

# Resolve o erro de 'index'
def index(request):
    return render(request, 'index.html')

# Resolve o erro de 'categoria'
def categoria(request):
    contexto = {
        'lista': Categoria.objects.all().order_by('-id'),
    }
    return render(request, 'categoria/lista.html', contexto)

def form_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Operação realizada com Sucesso')
            return redirect('categoria')
    else:
        form = CategoriaForm()
    return render(request, 'categoria/formulario.html', {'form': form})

# Resolve o erro de 'editar_categoria'
def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, pk=id) # Busca o objeto
    if request.method == 'POST':
        # instance=categoria garante a ATUALIZAÇÃO em vez de novo registro
        form = CategoriaForm(request.POST, instance=categoria) 
        if form.is_valid():
            form.save()
            messages.success(request, 'Operação realizada com Sucesso')
            return redirect('categoria')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'categoria/formulario.html', {'form': form})

# Resolve o erro de 'remover_categoria'
def remover_categoria(request, id):
    try:
        categoria = Categoria.objects.get(pk=id)
        categoria.delete()
        messages.success(request, 'Operação realizada com Sucesso')
    except Categoria.DoesNotExist:
        messages.error(request, 'Registro não encontrado')
    return redirect('categoria')

# Resolve o erro de 'detalhes_categoria'
def detalhes_categoria(request, id):
    categoria = get_object_or_404(Categoria, pk=id)
    return render(request, 'categoria/detalhes.html', {'item': categoria})
