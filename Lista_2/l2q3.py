print('Iremos calcular se calcular se João Papo-de-Pescador vai precisar multa pelo excesso de peso dos seus peixes!')
peso = int(input('Digite o peso do peixe: '))
if(peso > 50):
    excesso = peso - 50
    multa = excesso * 4
else:
    excesso = 0
    multa = 0
print(f'O valor do excesso é de {excesso} quilos e o valor da multa é de {multa} reais!')
