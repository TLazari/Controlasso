from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('app_controlasso.urls')),  # Ajuste o app conforme seu projeto
    path('', RedirectView.as_view(url='/api/')),   # Redireciona raiz (/) para /api/
]
