from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mi_aplicacion.urls')),  # Incluyendo las URLs de la aplicación 'mi_aplicacion'
    # Agrega más URLs de nivel superior según sea necesario
]
