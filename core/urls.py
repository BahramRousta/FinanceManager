from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-accounts/v1/', include('accounts.urls')),
    path('api-transition/v1/', include('transition.urls')),
    path('api-social_authentication/v1/', include('social_authentication.urls')),
]
