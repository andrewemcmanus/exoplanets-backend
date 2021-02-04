from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import Visual, User, Notes
from rest_framework.validators import UniqueValidator

class VisualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visual
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    # profile = ProfileSerializer()
    class Meta:
        model = User
        fields = '__all__'

    # def create(self, validated_data):
        # profile_data = validated_data.pop('profile')
        # user = User.objects.create(**validated_data)
        # Profile.objects.create(user=user, **profile_data)
        # return user

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'
