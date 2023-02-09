import random


lista = list(range(0,6))
result = []
dados = list(range(0,5))

for res in dados:
    for x in lista:
        num = random.randrange(1,61)
        if num not in result:
            result.append(num)

    
    print(sorted(result))
    result.clear()