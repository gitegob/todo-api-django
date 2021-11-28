from rest_framework import serializers
from todos.models import Todo


class CreateTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('title', 'description', 'is_complete')


class GetTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('__all__')
