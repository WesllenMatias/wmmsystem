from mega import Mega
from pprint import pprint


email = 'wesllen.matias@hotmail.com'
senha = '2qybcjqw@WMM'

mega = Mega()

mg = mega.login(email,senha)

def tot_usado():
    cota = mg.get_storage_space(giga=True)

    usado = cota['used']

    total_usado = round(usado,2)
    
    total_usado = {'total_usado':f'{total_usado}'}

    return total_usado

   


def arquivos():
    files = mg.get_files()
    #arq = files['xYcBia4D']['a']['n']
    for arq in files:
        print(files[arq]['a']['n'])


