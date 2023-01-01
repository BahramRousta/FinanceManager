from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="FinanceManagerAPI",
        default_version='v1',
        description="API for the FinanceManager app",
        contact=openapi.Contact(email="contact@snippets.local"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('api-accounts/v1/', include('accounts.urls')),
    path('api-transition/v1/', include('transition.urls')),
    path('api-social_authentication/v1/', include('social_authentication.urls')),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
