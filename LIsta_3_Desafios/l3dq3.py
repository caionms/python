print('Iremos verificar se um número é primo.')
num = int(input('Digite o número: '))
lista = []
for i in range(1, num + 1):
    if num % i == 0:
        lista.append(i)
if(len(lista) == 2):
    print('O número ',num, ' é primo.')
else:
    print('O número ',num, ' não é primo.')
