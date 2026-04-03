from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .models import User
from .serializers import UserSerializer,register_request_serializer
from rest_framework.authtoken.models import Token
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(method='post', request_body=register_request_serializer)
@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()

        return Response({
            "message": "User registered successfully",
            "data": {
                "id": user.id,
                "username": user.username,
                "role": user.role
            }
        }, status=201)

    return Response({
        "message": "Registration failed",
        "errors": serializer.errors
    }, status=400)


@swagger_auto_schema(method='post', request_body=register_request_serializer)
@api_view(['POST'])
def login(request):
    user = authenticate(
        username=request.data.get('username'),
        password=request.data.get('password')
    )

    if user:
        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            "message": "Login successful",
            "token": token.key,
            "user": {
                "id": user.id,
                "username": user.username,
                "role": user.role
            }
        })

    return Response({
        "message": "Invalid credentials"
    }, status=400)