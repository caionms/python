print('Iremos calcular o pagamento ideal.')
#print('Iremos calcular o troco ideal para um pagamento.')
valor = int(input('Digite o valor da conta: '))
#pag = int(input('Digite o valor pago: '))
n50 = n20 = n10 = n5 = n2 = n1 = 0
if(valor >= 50):
    n50 = valor // 50
    valor = valor % 50
if(valor >= 20):
    n20 = valor // 20
    valor = valor % 20
if(valor >= 10):
    n10 = valor // 10
    valor = valor % 10
if(valor >= 5):
    n5 = valor // 5
    valor = valor % 5
if(valor >= 2):
    n2 = valor // 2
    valor = valor % 2
if(valor >= 1):
    n1 = valor // 1
    valor = valor % 1
print(f'O pagamento ideal é de {n50} notas de 50 reais, {n20} notas de 20 reais, {n10} notas de 10 reais, {n5} notas de 5 reais, {n2} notas de 2 reais e {n1} notas de 1 real.')
