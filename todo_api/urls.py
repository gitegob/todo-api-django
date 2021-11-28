from django.contrib import admin
from django.urls import path, include
from todo_api.views import ping
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Todo API",
        default_version='v1',
        description="Api for a todo app",
        contact=openapi.Contact(email="briangitego@awesomity.rw"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=[]
)

urlpatterns = [
    path('', ping),
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    path('api/todos/', include('todos.urls')),

    # Swagger URLS
    path('docs/swagger-ui', schema_view.with_ui('swagger',
                                                cache_timeout=0), name='schema-swagger-ui'),
]
