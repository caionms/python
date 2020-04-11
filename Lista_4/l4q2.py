import random
print('Iremos sortear 20 inteiros entre 1 e 100, iremos separar e armazenar os pares e os ímpares em listas separadas.')
lista = []
lpar = []
limp = []
for x in range(20):
    lista.append(random.randrange(1,100))
for x in lista:
    if(x%2==0):
        lpar.append(x)
    else:
        limp.append(x)
lista.sort()
lpar.sort()
limp.sort()
print(f'A lista completa é {lista}.\nA lista dos pares é {lpar}.\nA lista dos ímpares é {limp}.')
