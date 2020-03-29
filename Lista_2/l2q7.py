print('Iremos calcular a quantidades de latas de tinta a serem compradas!')
m2 = int(input('Digite o tamanho em metros quadrados da área a ser pintada: '))
if(m2 <= 54):
    print(f'Será necessário 1 lata de tinta e o valor total é de 80 reais!')
elif(m2 % 54 == 0):
    print(f'Serão necessário {m2 // 54} latas de tinta e o valor total será de {(m2 // 54) * 80} reais!')
else:
    print(f'Serão necessário {(m2 // 54) + 1} latas de tinta e o valor total será de {((m2 // 54) + 1) * 80} reais!')
    
