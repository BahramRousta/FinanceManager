import uuid
from abc import ABC

from rest_framework import serializers
from .models import Otp


class OtpRequestSerializer(serializers.Serializer):
    """
        get user phone number for create an otp
    """
    phone_number = serializers.CharField(max_length=11, allow_null=False, required=True)


class RequestOtpResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Otp
        fields = ['request_id']


class VerifyOtpRequest(serializers.ModelSerializer):
    request_id = serializers.UUIDField(allow_null=False)

    class Meta:
        model = Otp
        fields = ['request_id', 'phone_number', 'code']
        extra_kwargs = {'code': {'required': True}}


class ObtainTokenSerializer(serializers.Serializer):
    access_token = serializers.CharField(max_length=255)
    refresh_token = serializers.CharField(max_length=255)
