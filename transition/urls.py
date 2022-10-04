from django.urls import path
from .views import (
    SingleTransitionAPIView,
    MultiTransitionAPIView,
    TransitionListAPIView,
    RetrieveTransitionAPIView,
    UpdateTransitionAPIView,
    DeleteTransitionAPIView,
    )

app_name = 'transition'

urlpatterns = [
    path('create-single-transition/', SingleTransitionAPIView.as_view(), name="create-single-transition"),
    path('create-multi-transition/', MultiTransitionAPIView.as_view(), name="create-multi-transition"),
    path('transition-list/', TransitionListAPIView.as_view(), name="transition-list"),
    path('retrieve-transition/<int:pk>', RetrieveTransitionAPIView.as_view(), name="retrieve-transition"),
    path('update-transition/<int:pk>', UpdateTransitionAPIView.as_view(), name="update-transition"),
    path('delete-transition/<int:pk>', DeleteTransitionAPIView.as_view(), name="delete-transition"),
]
