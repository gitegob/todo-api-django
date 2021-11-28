from django.urls import path
from todos.views import SearchTodosView, TodoView, TodosView

urlpatterns = [
    path('', TodosView.as_view()),
    path('search', SearchTodosView.as_view()),
    path('<int:todo_id>', TodoView),
]
