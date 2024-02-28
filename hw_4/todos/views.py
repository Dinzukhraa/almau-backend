from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST
from .models import TodoList, Todos
from .forms import TodoListForm, TodoForm
@require_GET
def index(request):
    return redirect('todo-lists')

@require_GET
def todo_lists(request):
    todo_lists = TodoList.objects.all()
    form = TodoListForm()

    return render(request, 'todo_lists.html', {'todo_lists': todo_lists, 'form': form})

@require_GET
def todo_list_detail(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    todos = Todos.objects.filter(todo_list=todo_list)
    return render(request, 'todo_list_detail.html', {'todo_list': todo_list, 'todos': todos})

@require_POST
def create_todo_list(request):
    form = TodoListForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('todo-lists')

@require_POST
def edit_todo_list(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    form = TodoListForm(request.POST, instance=todo_list)
    if form.is_valid():
        form.save()
        return redirect('todo-lists')
    return render(request, 'edit_todo_list.html', {'form': form, 'todo_list': todo_list})

@require_GET
def delete_todo_list(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    todo_list.delete()
    return redirect('todo-lists')

@require_GET
def delete_todo(request, id):
    todo = get_object_or_404(Todos, id=id)
    todo_list_id = todo.todo_list.id
    todo.delete()
    return redirect('todo-list-detail', id=todo_list_id)

@require_POST
def edit_todo(request, id):
    todo = get_object_or_404(Todos, id=id)
    form = TodoForm(request.POST, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('todo-list-detail', id=todo.todo_list.id)
    return render(request, 'edit_todo.html', {'form': form, 'todo': todo})

