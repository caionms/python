import random

l_total = []
l_par = []
l_impar = []

for i in range (1, 21):
    numero = random.randrange(1, 101)
    l_total.append(numero)
    if numero % 2 == 0:
        l_par.append(numero)
    else:
        l_impar.append(numero)
        
l_total.sort()
l_par.sort()
l_impar.sort()
        
print(l_total)
print(l_par)
print(l_impar)
