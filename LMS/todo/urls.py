from django.urls import path
from . import views

urlpatterns = [
    path('create', views.CreateTodo.as_view(), name="create_todo"),
    path('tododelete/<int:pk>', views.DeleteTodo.as_view(), name="todo_delete"),
]

