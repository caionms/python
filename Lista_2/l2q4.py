print('Iremos identificar qual dos três números é maior!')
lista = ["","",""]
lista[0] = int(input('Digite o primeiro número: '))
lista[1] = int(input('Digite o segundo número: '))
lista[2] = int(input('Digite o terceiro número: '))
lista.sort()
print(f'O maior número é {lista[2]}!')
