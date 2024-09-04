from django.shortcuts import render
from accountsapp.serializers import UserSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from knox.models import AuthToken
from knox.auth import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken

class UserRegistrationView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'token': AuthToken.objects.create(user)[1]
        }, status=status.HTTP_201_CREATED)


class UserLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        _, token = AuthToken.objects.create(user)  
        return Response({
            'token': token,
            'user_id': user.pk,
            'email': user.email
        }, status=status.HTTP_200_OK)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication] 

    def post(self, request):
        request._auth.delete()
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
