from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chaining/', include('smart_selects.urls')),
    path('', include('apps.cadastros.urls')),
    path('', include('apps.contratos.urls')),
    path('', include('apps.usuarios.urls')),
]
