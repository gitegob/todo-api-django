from rest_framework import serializers
from authentication.models import User


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email',
                  'password')
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if(password is not None):
            instance.set_password(password)
        instance.save()
        return instance


class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'password', 'access_token']
        read_only_fields = ['access_token ']
        extra_kwargs = {
            'email': {'write_only': True},
            'password': {'write_only': True}
        }
