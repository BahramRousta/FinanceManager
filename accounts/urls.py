from django.urls import path
from .views import (
    RegisterApiView,
    LogOut
)

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterApiView.as_view(), name='register'),
    path('logout/', LogOut.as_view(), name='logout'),
]