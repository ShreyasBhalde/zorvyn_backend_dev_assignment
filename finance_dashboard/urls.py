from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path

schema_view = get_schema_view(
    openapi.Info(
        title="Finance API",
        default_version='v1',
        description="Finance Dashboard API",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('users/', include('users.urls')),
    path('records/', include('records.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
]