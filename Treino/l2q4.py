print('Iremos identificar qual dos três números é maior!')
lista = []
a,b,c = input('Digite os 3 números: ').split()
lista.append(a)
lista.append(b)
lista.append(c)
lista.sort()
print(f'O maior valor é {lista[2]}.')
