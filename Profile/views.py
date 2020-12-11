from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserProfileSerializer
from rest_framework import status, viewsets
from .models import UserProfile
from rest_framework.authentication import TokenAuthentication
from .permissions import UserOwnObjectPermission


# Create your views here.



class UserProfileView(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    permission_classes = [
        UserOwnObjectPermission,

    ]
    authentication_classes = [
        TokenAuthentication,

    ]
