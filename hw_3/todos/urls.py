from django.urls import path
from .views import todo_list, todo_detail, create_todo, delete_todo

urlpatterns = [
    path('todos/', todo_list, name='todo_list'),
    path('todos/<int:id>/', todo_detail, name='todo_detail'),
    path('todos/create/', create_todo, name='create_todo'),
    path('todos/<int:id>/delete/', delete_todo, name='delete_todo'),
]