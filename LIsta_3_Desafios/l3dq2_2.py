print('Iremos calcular o troco ideal para um pagamento.')
valor = int(input('Digite o valor da conta: '))
pag = int(input('Digite o valor pago: '))
while(valor > pag):
    print('Valor insuficiente para o pagamento!')
    pag = int(input('Digite o valor pago: '))
troco = pag - valor
notas = [50, 20, 10, 5, 2, 1]
for nota in notas:
    while troco >= nota:
        print ('Uma nota de %d' %nota)   
        troco -= nota

