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
    # Sort the red line data by order
    metro_info = sortMetro(response, my_own_order)
    # Process the red line data
    metros = processMetro(metro_info, '38')

    return render(request, 'base/table.html', {'metros': metros})


def verde(request):
    # Get the green line data
    response = requests.get(
        'https://api.metrolisboa.pt:8243/estadoServicoML/1.0.1/tempoEspera/Linha/Verde',
        headers={'Authorization': 'Bearer ' + os.getenv('API_KEY')})

    # Green line order
    my_own_order = ['TE', 'CG', 'AL', 'RM', 'AE',
                    'AM', 'AR', 'AN', 'IN', 'MM', 'RO', 'BC', 'CS']

    # Sort the green line data by order
    metro_info = sortMetro(response, my_own_order)

    metros = processMetro(metro_info, '50')

    return render(request, 'base/table.html', {'metros': metros})


def azul(request):
    # Get the blue line data
    response = requests.get(
        'https://api.metrolisboa.pt:8243/estadoServicoML/1.0.1/tempoEspera/Linha/Azul',
        headers={'Authorization': 'Bearer ' + os.getenv('API_KEY')})

    # Blue line order
    my_own_order = ['RB', 'AS', 'AF', 'PO', 'CA', 'CM', 'AH', 'LA', 'JZ', 'PE',
                    'SS', 'PA', 'MP', 'AV',  'RE', 'BC', 'TP', 'SP']

    # Sort the blue line data by order
    metro_info = sortMetro(response, my_own_order)
    # Process the blue line data
    metros = processMetro(metro_info, '33')

    return render(request, 'base/table.html', {'metros': metros})


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
    print("\n\n\n\n\n")
    # Sort the yellow line data by order
    metro_info = sortMetro(response, my_own_order)
    for y in metro_info:
        print(y)
    # Process the yellow line data
    metros = processMetro(metro_info, '43')

    return render(request, 'base/table.html', {'metros': metros})
