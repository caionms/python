from collections import defaultdict

numero = int(input('Insira o número a ser decomposto: '))

dic_primos =  defaultdict(lambda: 0)

divisor = 2

while(True):
    if (numero == 1):
        break
    elif(numero % divisor == 0):
        numero = numero / divisor
        dic_primos[divisor] = dic_primos[divisor] + 1
    else:
       divisor = divisor + 1

for key in dic_primos:
    print(f'O primo {key} e sua multiplicidade eh {dic_primos[key]}!')
