from django.urls import path
from . import views
from .views import TodoListView, TodoCreateView

urlpatterns = [
    path('', TodoListView.as_view(), name='todo-list'),
    path('todo/create/', TodoCreateView.as_view(), name='todo-create'),
    path('todo/<int:id>/categorize/', views.categorize_todo, name='categorize-todo'),
    path('todo/<int:id>/edit/', views.edit_todo, name='edit-todo'),
    path('todo/<int:id>/delete/', views.delete_todo, name='delete-todo'),
    path('category/<int:category_id>/create-todo/', views.create_todo_for_category, name='create-todo-for-category'),
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
]
