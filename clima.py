import requests
import json


def clima_atual():

    url = "https://api.open-meteo.com/v1/forecast?latitude=-5.79&longitude=-35.21&hourly=temperature_2m"

    get_clima = requests.get(url)

    json_clima = get_clima.json()

    tamanho = len(json_clima['hourly']['temperature_2m'])

    temperatura = json_clima['hourly']['temperature_2m'][tamanho - 1]

    temp = {'temperatura': f'{temperatura} °C '}

    return temp

    #print(json_clima['hourly']['temperature_2m'][tamanho - 1])

#clima_atual()