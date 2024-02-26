from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Agrega más URLs según sea necesario

]

