import requests

def get_preco_combustivel(estado, produto):
    url = "http://www.anp.gov.br/preco/prc/Resumo_Semanal_Index.asp"
    params = {
        "selEstado": estado,
        "descSemana": "",
        "descProduto": produto,
        "codSemana": "",
        "tipoProduto": "1",
        "ano": "",
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        for item in data["series"]:
            if item["nome"] == "NATAL":
                preco = item["valor"]
                return preco
    else:
        return None

estado = "RN"

preco_gasolina = get_preco_combustivel(estado, "GASOLINA COMUM")
preco_etanol = get_preco_combustivel(estado, "ETANOL HIDRATADO")
preco_diesel = get_preco_combustivel(estado, "ÓLEO DIESEL")

if preco_gasolina:
    print(f"Preço da gasolina em Natal: R$ {preco_gasolina}")
else:
    print("Não foi possível obter os dados da ANP para a gasolina.")

if preco_etanol:
    print(f"Preço do etanol em Natal: R$ {preco_etanol}")
else:
    print("Não foi possível obter os dados da ANP para o etanol.")

if preco_diesel:
    print(f"Preço do diesel em Natal: R$ {preco_diesel}")
else:
    print("Não foi possível obter os dados da ANP para o diesel.")
