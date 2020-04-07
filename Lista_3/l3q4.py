print('Iremos calcular um número na sequência de Fibonacci de acordo com seu índice.')
ind = int(input('Digite o índice: '))
ant1 = 1
ant2 = 1
if(ind == 1 or ind == 2):
    print('O valor é 1.')
else:
    for x in range(3, ind+1):
        ant1, ant2 = (ant1 + ant2), ant1
    print(f'O valor é {ant1}.')
