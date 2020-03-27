print('Iremos calcular a redução do tempo de vida de um fumante!')
qnt_cig = int(input('Digite a quantidade de cigarros fumados por dia: '))
qnt_ano = int(input('Digite a quantos anos se é fumante: '))
temp = (qnt_cig * (qnt_ano * 365)) * 10
print(f'O total de dias perdido por esse fumante é de {temp}!')
