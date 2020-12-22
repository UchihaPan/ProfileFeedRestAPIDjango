from django.shortcuts import render
from rest_framework.response import Response
from .serializers import UserProfileSerializer,UserFeedserializer
from rest_framework import status, viewsets
from .models import UserProfile,ProfileFeedItem
from rest_framework.authentication import TokenAuthentication
from .permissions import UserOwnObjectPermission,UserOwnStatusPermission
from rest_framework.filters import SearchFilter
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticatedOrReadOnly




class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })



class UserProfileView(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    permission_classes = [
        UserOwnObjectPermission,

    ]
    authentication_classes = [
        TokenAuthentication,

    ]
    filter_backends = (SearchFilter,)
    search_fields=('name','email',)


class ProfileFeedView(viewsets.ModelViewSet):
    serializer_class = UserFeedserializer
    queryset = ProfileFeedItem.objects.all()
    authentication_classes = [
        TokenAuthentication,
    ]
    permission_classes = [
        UserOwnStatusPermission,
        IsAuthenticatedOrReadOnly,
    ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
