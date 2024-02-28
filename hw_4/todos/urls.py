from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('todo-lists/', todo_lists, name='todo-lists'),
    path('todo-lists/<int:id>/', todo_list_detail, name='todo-list-detail'),
    path('todo-lists/<int:id>/delete/', delete_todo_list, name='delete-todo-list'),
    path('todo-lists/<int:id>/edit/', edit_todo_list, name='edit-todo-list'),
    path('todos/<int:id>/delete/', delete_todo, name='delete-todo'),
    path('todos/<int:id>/edit/', edit_todo, name='edit-todo'),
    path('create-todo-list/', create_todo_list, name='create-todo-list'),
]