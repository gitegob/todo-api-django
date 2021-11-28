from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.exceptions import NotFound
from django.db.models import Q
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import GenericAPIView
from todos.serializers import CreateTodoSerializer, GetTodoSerializer
from todos.models import Todo


class TodosView(GenericAPIView):
    authentication_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(responses={'200': [GetTodoSerializer]})
    def get(self, request) -> Response:
        qs = Todo.objects.filter(owner=request.user)
        serializer = GetTodoSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=CreateTodoSerializer)
    def post(self, request) -> Response:
        serializer = CreateTodoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TodoView(GenericAPIView):
    authentication_classes = [permissions.IsAuthenticated]

    def get(self, request, todo_id):
        serializer = GetTodoSerializer(self.find_todo(request, todo_id))
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, todo_id):
        todo = self.find_todo(request, todo_id)
        update_serializer = CreateTodoSerializer(
            todo, data=request.data, partial=True)
        update_serializer.is_valid(raise_exception=True)
        update_serializer.save()
        return Response(update_serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, todo_id):
        todo = self.find_todo(request, todo_id)
        todo.delete()
        return Response("Todo deleted", status=status.HTTP_200_OK)

    def find_todo(self, request, todo_id):
        todo: Todo = Todo.objects.filter(
            owner=request.user, id=todo_id).first()
        if not todo:
            raise NotFound('Todo not found')
        return todo


class SearchTodosView(GenericAPIView):
    def get(self, request):
        q = request.query_params.get('q', None)
        todos = Todo.objects.filter(
            Q(title__icontains=q) | Q(description__icontains=q))
        serializer = GetTodoSerializer(todos, many=True)
        return Response(serializer.data)
