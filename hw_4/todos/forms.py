from django import forms
from .models import Todo, TodoList

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'due_date', 'status']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }

class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['title', 'description']