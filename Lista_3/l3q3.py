print(f'Iremos calcular o número de anos necessários para que a população do país A:\n{"Habitantes: ": <11}80000\n{"Taxa anual de crescimento: ": <27}3%')
print(f'Ultrapasse ou iguale a população do país B:\n{"Habitantes: ": <11}200000\n{"Taxa anual de crescimento: ": <27}1,5%')
popA, popB, ano = 80000, 200000, 0
tcA, tcB = 0.03, 0.015
while(popA < popB):
    ano += 1
    popA += (popA * tcA)
    popB += (popB * tcB)
    print('Ano: ', ano)
    print('  Cidade A:\n    Habitantes: %.0f' % popA)
    #"%.0f' % popA'" % é representando o valor .0f é a quantidade de números após a vírgula % popA é o operador apontando para o valor
    print('  Cidade B:\n    Habitantes: %.0f' % popB)
print(f'No ano {ano} a população da cidade A ultrapassou a população da cidade B.')
