from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Visual
from rest_framework.validators import UniqueValidator

class VisualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visual
        fields = '__all__'
        
