from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status, permissions, generics
from authentication.serializers import LoginSerializer, SignupSerializer

# Create your views here.


class Signup(generics.GenericAPIView):
    authentication_classes = []

    @swagger_auto_schema(request_body=SignupSerializer, operation_description="Sign up")
    def post(self, request) -> Response:
        serializer = SignupSerializer(
            data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class Login(generics.GenericAPIView):
    authentication_classes = []

    @swagger_auto_schema(request_body=LoginSerializer, responses={"200": LoginSerializer}, operation_description="Sign up")
    def post(self, request) -> Response:
        email = request.data['email']
        password = request.data['password']
        user = authenticate(username=email, password=password)
        if not user:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = LoginSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetUser(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request) -> Response:
        user = request.user
        serializer = SignupSerializer(user)
        return Response(serializer.data)
