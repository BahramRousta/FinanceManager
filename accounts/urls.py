from django.urls import path
from .views import (
    RegisterApiView,
    LogOut
)
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterApiView.as_view(), name='register'),
    path('logout/', LogOut.as_view(), name='logout'),

    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]