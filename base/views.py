import requests
from dotenv import load_dotenv
import os
from django.shortcuts import render

# Create your views here.
load_dotenv()


def vermelha(request):
    response = requests.get(
        'https://api.metrolisboa.pt:8243/estadoServicoML/1.0.1/tempoEspera/Linha/Vermelha',
        headers={'Authorization': 'Bearer ' + os.getenv('API_KEY')},
    )
    return render(request, 'base/table.html', {'response': response.json()["resposta"]})


def verde(request):
    response = requests.get(
        'https://api.metrolisboa.pt:8243/estadoServicoML/1.0.1/tempoEspera/Linha/Verde',
        headers={'Authorization': 'Bearer ' + os.getenv('API_KEY')},
    )
    return render(request, 'base/table.html', {'response': response.json()["resposta"]})


def azul(request):
    response = requests.get(
        'https://api.metrolisboa.pt:8243/estadoServicoML/1.0.1/tempoEspera/Linha/Azul',
        headers={'Authorization': 'Bearer ' + os.getenv('API_KEY')},
    )
    return render(request, 'base/table.html', {'response': response.json()["resposta"]})


def amarela(request):
    response = requests.get(
        'https://api.metrolisboa.pt:8243/estadoServicoML/1.0.1/tempoEspera/Linha/Amarela',
        headers={'Authorization': 'Bearer ' + os.getenv('API_KEY')},
    )
    return render(request, 'base/table.html', {'response': response.json()["resposta"]})
