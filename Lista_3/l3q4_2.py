numero = int(input('Insira o numero para a sequencia de fibonacci: '))
    
antigo_valor = 0
    
novo_valor = 1

for i in range (2, numero+1):
    antigo_valor, novo_valor = novo_valor, (antigo_valor + novo_valor)
    
print(f'O numero de Fibonacci de {numero} eh {novo_valor}!')
