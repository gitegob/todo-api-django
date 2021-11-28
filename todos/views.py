from rest_framework import permissions, response, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import NotFound
from django.db.models import Q
from drf_yasg.utils import swagger_auto_schema

from todos.serializers import CreateTodoSerializer, GetTodoSerializer
from todos.models import Todo

# Create your views here.


@swagger_auto_schema(methods=['post'], request_body=CreateTodoSerializer)
@api_view(['GET', 'POST'])
@permission_classes((permissions.IsAuthenticated,))
def get_create_todo(request):
    if request.method == 'GET':
        qs = Todo.objects.filter(owner=request.user)
        serializer = GetTodoSerializer(qs, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = CreateTodoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.IsAuthenticated,))
def get_update_delete_todo(request, todo_id):
    todo: Todo = Todo.objects.filter(owner=request.user, id=todo_id).first()
    if not todo:
        raise NotFound('Todo not found')
    serializer = GetTodoSerializer(todo)
    if request.method == 'GET':
        return response.Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        update_serializer = CreateTodoSerializer(
            todo, data=request.data, partial=True)
        update_serializer.is_valid(raise_exception=True)
        update_serializer.save()
        return response.Response(update_serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        todo.delete()
        return response.Response("Todo deleted", status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((permissions.IsAuthenticated,))
def search_todos(request):
    q = request.query_params.get('q', None)
    todos = Todo.objects.filter(
        Q(title__icontains=q) | Q(description__icontains=q))
    serializer = GetTodoSerializer(todos, many=True)
    return response.Response(serializer.data)
