from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
from .forms import TodoForm

# Получение всех задач
def get_todos(request):
    todos = Todo.objects.all()
    return render(request, 'todos/todo_list.html', {'todos': todos})

# Получение задачи по ID
def get_todo_by_id(request, id):
    todo = get_object_or_404(Todo, id=id)
    return render(request, 'todos/todo_detail.html', {'todo': todo})

# Создание задачи
def create_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_todos')
    else:
        form = TodoForm()
    return render(request, 'todos/todo_form.html', {'form': form})

# Удаление задачи
def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    return redirect('get_todos')




# Create your views here.
