from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Todo

def todos_list(request):
    todos = Todo.objects.all()
    data = [{'id': todo.id, 'title': todo.title, 'description': todo.description,
             'due_date': todo.due_date, 'status': todo.status} for todo in todos]
    return JsonResponse(data, safe=False)

def todo_detail(request, id):
    todo = get_object_or_404(Todo, id=id)
    data = {'id': todo.id, 'title': todo.title, 'description': todo.description,
            'due_date': todo.due_date, 'status': todo.status}
    return JsonResponse(data)

def create_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todos_list')
    else:
        form = TodoForm()

    return render(request, 'todos/todo_form.html', {'form': form})

def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    return redirect('todos_list')
