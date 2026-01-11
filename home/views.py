from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Categoria
from .forms import CategoriaForm

# Esta função DEVE existir para o servidor rodar 
def index(request):
    return render(request, 'index.html')

# View de Listagem
def categoria(request):
    contexto = {
        'lista': Categoria.objects.all().order_by('-id'),
    }
    return render(request, 'categoria/lista.html', contexto)

# View de Edição (Garante que o registro seja ATUALIZADO e não duplicado)
def editar_categoria(request, id):
    try:
        categoria = Categoria.objects.get(pk=id)
    except Categoria.DoesNotExist:
        messages.error(request, 'Registro não encontrado')
        return redirect('categoria')

    if request.method == 'POST':
        # O uso de instance=categoria é o que impede a criação de um novo registro ao editar
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Operação realizada com Sucesso')
            return redirect('categoria')
    else:
        form = CategoriaForm(instance=categoria)
    
    return render(request, 'categoria/formulario.html', {'form': form})

# View de Criação
def form_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria criada com sucesso!')
            return redirect('categoria')
    else:
        form = CategoriaForm()

    return render(request, 'categoria/formulario.html', {'form': form})
