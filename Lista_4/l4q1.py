import random
print('Iremos sortear 10 inteiros entre 1 e 100 e descobrir o maior e o menor elemento.')
lista = []
for x in range(10):
    lista.append(random.randrange(1, 100))
print(f'Os números são {lista}.')
lista.sort()
print(f'O menor elemento é {lista[0]} e o maior elemento é {lista[9]}.')

