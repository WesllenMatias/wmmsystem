import requests
import json




def cotacao_atual(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}"
    get_cotacao = requests.get(url)
    json_cotacao = get_cotacao.json()
    cotacao = json_cotacao["USDBRL"]["bid"]
    cotacao = float(cotacao)
    cotacao = round(cotacao,2)
    cotacao = { 'cotacao': f'{cotacao}' }
    return cotacao


#cotacao_atual('USD-BRL')