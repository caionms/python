print('Iremos identificar o maior e menor número em três números!')
lista = []
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
lista.append(a)
lista.append(b)
lista.append(c)
lista.sort()
print(f'O menor elemento é {lista[0]} e o maior elemento é {lista[2]}')
               
