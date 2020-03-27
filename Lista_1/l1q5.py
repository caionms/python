print('Iremos calcular o valor de um desconto e o preço de uma mercadoria após aplicar o desconto.')
valor = int(input('Digite o valor da mercadoria: '))
desc = int(input('Digite a porcentagem do desconto: '))
val_desc = (valor * desc)/100
print(f'O valor do desconto é de {val_desc} reais!')
print(f'O valor da mercadoria após o desconto é de {valor - val_desc} reais!')
