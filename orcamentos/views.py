from django.shortcuts import render
from clima import clima_atual
from moedas import cotacao_atual
from checa_backups import tot_usado
# Create your views here.

def home(request):
    temperatura = clima_atual()
    cotacao = cotacao_atual('USD-BRL')
    total_usado = tot_usado()
    

    return render(request, "adminlte/index.html", { 'temperatura' : temperatura,
                                                     'cotacao':cotacao,
                                                     'total_usado': total_usado})