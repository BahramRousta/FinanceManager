from rest_framework import serializers
from .models import Transition


class CreateTransitionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transition
        fields = ['name', 'description', 'operation', 'bank', 'category', 'sub_category']


class UpdateTransitionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transition
        fields = ['name', 'description', 'operation', 'bank', 'category', 'sub_category']
