from django.urls import path
from rest_framework import views

from todos.views import get_create_todo, get_update_delete_todo, search_todos

urlpatterns = [
    path('', get_create_todo),
    path('search', search_todos),
    path('<int:todo_id>', get_update_delete_todo),
]
