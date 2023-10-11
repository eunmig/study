from django.shortcuts import render, redirect
from . models import Todo
from .forms import TodoForm
from django.views.decorators.http import require_http_methods

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    todos = Todo.objects.all()
    context = {
        'todos' : todos,
    }
    return render(request, 'todos/index.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.save()
            return redirect('todos:index')
    else:
        form = TodoForm()

    context = {
        'form' : form,
    }

    return render(request, 'todos/create.html', context)