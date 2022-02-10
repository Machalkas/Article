from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import UserSerializer, UserPermissionSerializer
from .models import User

class UserRegisterView(APIView):
    def post(self, request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

class UserView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, id):
        try:
            user=User.objects.get(pk=id)
        except:
            return Response(data={"detail":"Пользватель %s не найден"%id}, status=404)
        serializer=UserSerializer(user)
        return Response(serializer.data)

class UserPermissionView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]
    def put(self, request, id):
        try:
            user=User.objects.get(pk=id)
        except:
            return Response(data={"detail":"Пользватель %s не найден"%id}, status=404)
        serializer=UserPermissionSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        return Response(serializer.errors,status=400)

class ListUsersView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]
    def get(self, request):
        user=User.objects.all()
        serializer=UserSerializer(user, many=True)
        return Response(serializer.data)

class SelfView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        serializer=UserSerializer(request.user)
        return Response(serializer.data)