from django.http import HttpResponse


def index(request):
    return HttpResponse("¡Hola, mundo! Esta es la vista de inicio.")
# Create your views here.
