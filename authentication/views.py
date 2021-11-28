from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions
from authentication.serializers import LoginSerializer, SignupSerializer

# Create your views here.


# class RegisterAPIView(generics.GenericAPIView):
#     authentication_classes = []

#     serializer_class: SignupSerializer

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_201_CREATED)


@swagger_auto_schema(methods=['post'], request_body=SignupSerializer)
@api_view(['POST'])
@authentication_classes(())
def signup(request):
    serializer = SignupSerializer(
        data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status.HTTP_201_CREATED)


@swagger_auto_schema(methods=['post'], request_body=LoginSerializer)
@api_view(['POST'])
@authentication_classes(())
def login(request):
    email = request.data['email']
    password = request.data['password']
    user = authenticate(username=email, password=password)
    if not user:
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    serializer = LoginSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((permissions.IsAuthenticated,))
def get_user(request):
    user = request.user
    serializer = SignupSerializer(user)
    return Response(serializer.data)
