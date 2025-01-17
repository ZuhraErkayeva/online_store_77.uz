from django.contrib.auth import login,logout
from rest_framework.decorators import action
from rest_framework import viewsets,status
from rest_framework.response import Response
from .serializers import RegisterSerializer,LoginSerializer



class RegistrationViewSet(viewsets.ViewSet):
    @action(detail=False,methods=['post'])
    def register(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response("Ro'yhatdan o'tdingiz!", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False,methods=['post'])
    def login(self,request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data()
            login(request,user)
            return Response("Muvaffaqiyatli kirdingiz!", status=status.HTTP_200_OK)
        return Response("Qayerdadir xatolik bor", status=status.HTTP_400_BAD_REQUEST)

    def logout(self, request):
        login(request)
        return Response("Muvaffaqiyatli chiqdigiz!", status=status.HTTP_200_OK)
