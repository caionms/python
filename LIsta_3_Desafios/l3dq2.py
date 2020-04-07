print('Iremos calcular o troco ideal para um pagamento.')
valor = int(input('Digite o valor da conta: '))
pag = int(input('Digite o valor pago: '))
while(valor > pag):
    print('Valor insuficiente para o pagamento!')
    pag = int(input('Digite o valor pago: '))
troco = pag - valor
n50 = n20 = n10 = n5 = n2 = n1 = 0
if(troco >= 50):
    n50 = troco // 50
    troco = troco % 50
if(troco >= 20):
    n20 = troco // 20
    troco = troco % 20
if(troco >= 10):
    n10 = troco // 10
    troco = troco % 10
if(troco >= 5):
    n5 = troco // 5
    troco = troco % 5
if(troco >= 2):
    n2 = troco // 2
    troco = troco % 2
if(troco >= 1):
    n1 = troco // 1
    troco = troco % 1
print('O troco ideal é composto de: ')
if(n50 != 0):
    print(f'{n50} notas de 50 reais ')
if(n20 != 0):
    print(f'{n20} notas de 20 reais ')
if(n10 != 0):
    print(f'{n10} notas de 10 reais ')
if(n5 != 0):
    print(f'{n5} notas de 5 reais ')
if(n2 != 0):
    print(f'{n2} notas de 2 reais ')
if(n1 != 0):
    print(f'{n1} notas de 1 real. ')
