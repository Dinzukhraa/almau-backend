from django import forms
from .models import TodoList, Todos

class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['title', 'description']

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todos
        fields = ['title', 'description', 'due_date', 'status', 'todo_list']
