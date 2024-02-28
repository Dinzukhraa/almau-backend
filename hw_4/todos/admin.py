from django.contrib import admin
from .models import TodoList, Todos


# Register your models here.
admin.site.register(TodoList)
admin.site.register(Todos)