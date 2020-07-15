print('Iremos contar quantos números são pares e divisíveis por 7 entre 1067 e 3627.')
count = 0
for num in range(1067, 3628):
    if(num % 2 == 0 and num % 7 == 0 ):
        count += 1
print(f'Existem {count} números que satisfazem.')
