import requests
from dotenv import load_dotenv
import os

# Create your views here.
from django.http import HttpResponse
load_dotenv()


def vermelha(request):
    response = requests.get(
        'https://api.metrolisboa.pt:8243/estadoServicoML/1.0.1/tempoEspera/Linha/Vermelha',
        headers={'Authorization': 'Bearer ' + os.getenv('API_KEY')},
    )
    return HttpResponse(response)


def verde(request):
    response = requests.get(
        'https://api.metrolisboa.pt:8243/estadoServicoML/1.0.1/tempoEspera/Linha/Verde',
        headers={'Authorization': 'Bearer ' + os.getenv('API_KEY')},
    )
    return HttpResponse(response)
