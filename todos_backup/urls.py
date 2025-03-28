from django.urls import path
from .views import register_view, login_view, todo_list, todo_detail, todo_create, todo_delete, logout_view


urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("todos/", todo_list, name="todo_list"),
    path("todos/<int:id>/", todo_detail, name="todo_detail"),
    path("todos/new/", todo_create, name="todo_create"),
    path("todos/<int:id>/delete/", todo_delete, name="todo_delete"),
]
