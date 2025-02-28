from django.shortcuts import get_object_or_404, redirect, render
from todos.forms import TodoForm, TodoListForm
from todos.models import Todo, TodoList
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def index(request):
    return redirect('todolist-list')

def todo_lists(request):
    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_lists')
    else:
        form = TodoListForm()
    todo_lists = TodoList.objects.all()
    return render(request, 'todos/todo_lists.html', {'todo_lists': todo_lists, 'form': form})

def todo_list_detail(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    todos = Todo.objects.filter(todo_list=todo_list)

    return render(request, 'todos/todo_list_detail.html', {'todo_list': todo_list, 'todos': todos})

def edit_todo_list(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    if request.method == 'POST':
        form = TodoListForm(request.POST, instance=todo_list)
        if form.is_valid():
            form.save()
            return redirect('todo_lists')
    else:
        form = TodoListForm(instance=todo_list)
    return render(request, 'todos/edit_todo_list.html', {'form': form})

def edit_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            if not todo.todo_list:
                todo.todo_list = None
            todo.save()
            return redirect('todo-list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todos/edit_todo.html', {'form': form, 'todo': todo})

# Добавляем функцию удаления списка дел
def delete_todo_list(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    todo_list.delete()
    return redirect('todo_lists')

# Добавляем функцию удаления задачи
def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    return redirect('todo-list')

class TodoListView(ListView):
    model = Todo
    template_name = 'todos/todo_list.html'
    context_object_name = 'todos'

class TodoCreateView(CreateView):
    model = Todo
    template_name = 'todos/todo_form.html'
    fields = ['title', 'description', 'due_date', 'status']
    success_url = reverse_lazy('todo-list')

    def form_valid(self, form):
        form.instance.todo_list = None  # Устанавливаем значение по умолчанию
        return super().form_valid(form)

def categorize_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == 'POST':
        category_id = request.POST.get('category')
        new_category = request.POST.get('new_category')
        
        if new_category:  # Если создаётся новая категория
            category = TodoList.objects.create(title=new_category)
            todo.todo_list = category
            todo.save()
            return redirect('todo-list')
        elif category_id:  # Если выбрана существующая категория
            category = TodoList.objects.get(id=category_id)
            todo.todo_list = category
            todo.save()
            return redirect('todo-list')
            
    categories = TodoList.objects.all()
    return render(request, 'todos/categorize_todo.html', {
        'todo': todo,
        'categories': categories
    })

def create_todo_for_category(request, category_id):
    category = get_object_or_404(TodoList, id=category_id)
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.todo_list = category
            todo.save()
            return redirect('todo-list')
    else:
        form = TodoForm()
    return render(request, 'todos/create_todo_for_category.html', {
        'form': form,
        'category': category
    })

class CategoryListView(ListView):
    model = TodoList
    template_name = 'todos/categories.html'
    context_object_name = 'categories'
