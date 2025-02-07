from django.urls import path
from .views import get_todos, get_todo_by_id, create_todo, delete_todo

urlpatterns = [
    path('', get_todos, name='get_todos'),
    path('<int:id>/', get_todo_by_id, name='get_todo_by_id'),
    path('add/', create_todo, name='create_todo'),
    path('<int:id>/delete/', delete_todo, name='delete_todo'),
]
