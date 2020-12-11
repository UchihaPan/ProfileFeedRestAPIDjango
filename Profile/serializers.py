from rest_framework import serializers
from .models import UserProfile
# Create your tests here.

class Helloserializers(serializers.Serializer):
    name=serializers.CharField(max_length=255)

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields=('email','name','password',)
        extra_kwargs= {'password': {'write_only': True,}}

    def create(self, validated_data):
        return UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
        )