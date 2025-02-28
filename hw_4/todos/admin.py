from django.contrib import admin
from .models import TodoList, Todo

@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'due_date', 'status', 'todo_list')
    list_filter = ('todo_list', 'status', 'due_date')
    search_fields = ('title', 'description', 'todo_list__title')
    list_editable = ('status',)

# Удаляем старые регистрации, так как используем декораторы
# admin.site.register(TodoList)
# admin.site.register(Todo)


# Register your models here.
