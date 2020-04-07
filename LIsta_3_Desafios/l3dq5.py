print('Iremos inverter um número inteiro positivo.')
num = str(input('Digite o número: '))
tam = len(num)
inv = num[tam-1]
for x in range(tam-1):
    inv += num[tam-2 - x]
print(f'O número invetido é {inv}.')
