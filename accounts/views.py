from django.contrib.auth import get_user_model, login
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.serializers import (
    OtpRequestSerializer,
    RequestOtpResponseSerializer,
    VerifyOtpRequest,
    ObtainTokenSerializer
)
from .models import Otp

User = get_user_model()


def _handle_login(otp, request):
    query = User.objects.filter(username=otp['phone_number'])
    if query.exists():
        user = query.first()
    else:
        user = User.objects.create(username=otp['phone_number'])

    refresh = RefreshToken.for_user(user)
    login(request, user=user)
    return ObtainTokenSerializer({
        'refresh_token': str(refresh),
        'access_token': str(refresh.access_token)
    }).data


class RegisterApiView(APIView):

    def get(self, request):
        serializer = OtpRequestSerializer(data=request.query_params)
        if serializer.is_valid():
            data = serializer.validated_data
            otp = Otp.objects.create(phone_number=data['phone_number'])
            print(otp.code)
            return Response(data=RequestOtpResponseSerializer(otp).data)
        else:
            return Response(data=serializer.errors)

    def post(self, request):
        serializer = VerifyOtpRequest(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            if Otp.objects.is_valid(data['request_id'], data['phone_number'], data['code']):
                return Response(_handle_login(data, request))
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

