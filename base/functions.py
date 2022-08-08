from time import strftime
from time import gmtime


def processMetro(metro_info, destino, estacoes):
    count = 0
    metros = []
    auxDic = {}
    for metro in metro_info:
        if metro['stop_id'] == 'OD' or metro['stop_id'] == 'RA':
            if metro['stop_id'] == 'OD':
                auxDic["tempoChegada1"] = strftime(
                    "%M:%S", gmtime(int(metro["tempoChegada1"])))
            else:
                auxDic["tempoChegada2"] = strftime(
                    "%M:%S", gmtime(int(metro["tempoChegada1"])))

            auxDic["stop_id"] = metro["stop_id"]
            metros.append(auxDic)
            auxDic = {}
            continue
        # For some reason this value is duplicated in the API
        if metro["cais"] == 'CS27O':
            continue
        auxDic["stop_id"] = metro["stop_id"]
        if metro["destino"] == destino:
            auxDic["tempoChegada2"] = strftime(
                "%M:%S", gmtime(int(metro["tempoChegada1"])))
            count += 1
        else:
            auxDic["tempoChegada1"] = strftime(
                "%M:%S", gmtime(int(metro["tempoChegada1"])))
            count += 1
        if count == 2:
            metros.append(auxDic)
            count = 0
            auxDic = {}
    
    i = 0
    for metro in metros:
        metro["nome"] = estacoes[i]
        i += 1
    return metros


def sortMetro(response, my_own_order):
    order = {key: i for i, key in enumerate(my_own_order)}
    metro_info = response.json()["resposta"]
    metro_info = sorted(metro_info, key=lambda d: order[d['stop_id']])
    return metro_info
