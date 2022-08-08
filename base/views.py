import requests
from dotenv import load_dotenv
import os
from django.shortcuts import render
from base.functions import processMetro, sortMetro

# Create your views here.
load_dotenv()


def vermelha(request):
    # Get the red line data
    response = requests.get(
        'https://api.metrolisboa.pt:8243/estadoServicoML/1.0.1/tempoEspera/Linha/Vermelha',
        headers={'Authorization': 'Bearer ' + os.getenv('API_KEY')})

    # Red line order
    my_own_order = ['SS', 'SA', 'AM', 'OL', 'BV',
                    'CH', 'OS', 'CR', 'OR', 'MO', 'EN', 'AP']
    # Red line stations
    stations = ['São Sebastião', 'Saldanha', 'Alameda', 'Olaias', 'Bela Vista', 'Chelas',
                'Olivais', 'Cabo Ruivo', 'Oriente', 'Moscavide', 'Encarnação', 'Aeroporto']
    # Sort the red line data by order
    metro_info = sortMetro(response, my_own_order)
    # Process the red line data
    metros = processMetro(metro_info, '38', stations)

    return render(request, 'base/table.html', {'metros': metros,
                                               'sentido2': "São Sebastião -> -> -> Aeroporto ",
                                               'sentido1': "Aeroporto -> -> -> São Sebastião"})


def verde(request):
    # Get the green line data
    response = requests.get(
        'https://api.metrolisboa.pt:8243/estadoServicoML/1.0.1/tempoEspera/Linha/Verde',
        headers={'Authorization': 'Bearer ' + os.getenv('API_KEY')})

    # Green line order
    my_own_order = ['TE', 'CG', 'AL', 'RM', 'AE',
                    'AM', 'AR', 'AN', 'IN', 'MM', 'RO', 'BC', 'CS']
    # Green line stations
    stations = ['Telheiras',
                'Campo Grande', 'Alvalade', 'Roma', 'Areeiro', 'Alameda',
                'Arroios', 'Anjos', 'Intendente', 'Martim Moniz', 'Rossio',
                'Baixa-Chiado', 'Cais do Sodré']

    # Sort the green line data by order
    metro_info = sortMetro(response, my_own_order)

    metros = processMetro(metro_info, '50', stations)

    return render(request, 'base/table.html', {'metros': metros,
                                               'sentido2': "Cais do Sodré -> -> -> Telheiras ",
                                               'sentido1': "Telheiras -> -> -> Cais do Sodré"})


def azul(request):
    # Get the blue line data
    response = requests.get(
        'https://api.metrolisboa.pt:8243/estadoServicoML/1.0.1/tempoEspera/Linha/Azul',
        headers={'Authorization': 'Bearer ' + os.getenv('API_KEY')})

    # Blue line order
    my_own_order = ['RB', 'AS', 'AF', 'PO', 'CA', 'CM', 'AH', 'LA', 'JZ', 'PE',
                    'SS', 'PA', 'MP', 'AV',  'RE', 'BC', 'TP', 'SP']
    # Blue line stations
    stations = ["Reboleira", "Amadora Este", "Alfornelos", "Pontinha",
                "Carnide", "Colégio Militar / Luz", "Alto dos Moinhos", "Laranjeiras",
                "Jardim Zoológico", "Praça de Espanha", "São Sebastião", "Parque",
                "Marquês do Pombal", "Avenida", "Restauradores", "Baixa-Chiado",
                "Terreiro do Paço", "Santa Apolónia"]

    # Sort the blue line data by order
    metro_info = sortMetro(response, my_own_order)
    # Process the blue line data
    metros = processMetro(metro_info, '33', stations)

    return render(request, 'base/table.html', {'metros': metros,
                                               'sentido1': "Santa Apolónia -> -> -> Reboleira ",
                                               'sentido2': "Reboleira -> -> -> Santa Apolónia"})


def amarela(request):
    response = requests.get(
        'https://api.metrolisboa.pt:8243/estadoServicoML/1.0.1/tempoEspera/Linha/Amarela',
        headers={'Authorization': 'Bearer ' + os.getenv('API_KEY')})

    x = response.json()["resposta"]
    for y in x:
        print(y)
    # Yellow line order
    my_own_order = ['OD', 'SR', 'AX', 'LU',
                    'QC', 'CG', 'CU', 'EC', 'CP', 'SA', 'PI', 'MP', 'RA']
    # Yellow line stations
    stations = ["Odivelas", "Senhor Roubado", "Ameixoeira", "Lumiar",
                "Quinta das Conchas", "Campo Grande", "Cidade Universitária",
                "Entre Campos", "Campo Pequeno", "Saldanha", "Picoas",
                "Marquês de Pombal", "Rato"]

    # Sort the yellow line data by order
    metro_info = sortMetro(response, my_own_order)
    # Process the yellow line data
    metros = processMetro(metro_info, '43', stations)

    return render(request, 'base/table.html', {'metros': metros,
                                               'sentido1': "Rato -> -> -> Odivelas ",
                                               'sentido2': "Odivelas -> -> -> Rato"})
