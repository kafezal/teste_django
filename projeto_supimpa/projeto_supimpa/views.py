from django.http import HttpResponse

def teste_view(request):
    return HttpResponse("Essa é a minha rota")

def index_view(request):
    return HttpResponse("bem vindo")