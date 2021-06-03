print('Iremos calcular a quantidade de latas de tinta a serem compradas.')
m2 = int(input('Digite o tamanho em metros quadrados da área a ser pintada:'))
if m2 <= 54:
    qtd_latas = 1
elif(m2%54==0):
    qtd_latas = m2//54
else:
    qtd_latas = m2//54+1
print(f'O número de latas foi {qtd_latas} e custou {qtd_latas*80} reais.')
