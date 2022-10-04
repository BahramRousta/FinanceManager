from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import (
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from rest_framework.permissions import IsAuthenticated
from accounts.models import CustomUser
from .pagination import TransitionListPagination
from .permission_mixin import IsOwnerTransition
from .serializers import (
    CreateTransitionSerializer,
    UpdateTransitionSerializer
)
from .models import Transition


def _get_user(request):
    user = CustomUser.objects.filter(username=request.user).first()
    return user


class SingleTransitionAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = CreateTransitionSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            transition = Transition.objects.create(owner=_get_user(request), **data)
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class MultiTransitionAPIView(APIView):

    def post(self, request):
        serializer = CreateTransitionSerializer(data=request.data, many=True)
        if serializer.is_valid():
            data = serializer.validated_data
            for index in data:
                transition = Transition.objects.create(owner=_get_user(request),
                                                       name=index['name'],
                                                       bank=index['bank'],
                                                       category=index['category'],
                                                       sub_category=index['sub_category'],
                                                       operation=index['operation']
                                                       )
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class TransitionListAPIView(APIView):
    permission_classes = ([IsAuthenticated])
    pagination_class = TransitionListPagination

    def get(self, request):
        try:
            transitions = Transition.objects.filter(owner=_get_user(request))
            if transitions:
                serializer = CreateTransitionSerializer(transitions, many=True)
                return Response(status=status.HTTP_200_OK, data=serializer.data)
        except:
            return Response(status=status.HTTP_403_FORBIDDEN)


class RetrieveTransitionAPIView(RetrieveAPIView):
    queryset = Transition.objects.all()
    serializer_class = CreateTransitionSerializer
    permission_classes = (IsOwnerTransition,)


class UpdateTransitionAPIView(UpdateAPIView):
    queryset = Transition.objects.all()
    serializer_class = UpdateTransitionSerializer
    permission_classes = (IsOwnerTransition,)


class DeleteTransitionAPIView(DestroyAPIView):
    queryset = Transition.objects.all()
    serializer_class = UpdateTransitionSerializer
    permission_classes = (IsOwnerTransition,)
