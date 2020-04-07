print('Iremos determinar o máximo divisor comum entre dois números inteiros positivos.')
n1 = num1 = int(input('Digite o primeiro número: '))
n2 = num2 = int(input('Digite o segundo número: '))
while(n1 % n2 != 0):
    n1, n2 = n2, n1 % n2
print(f'O mdc({num1},{num2})={n2}.')
