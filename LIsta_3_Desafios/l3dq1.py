print('Iremos conferir se um inteiro positivo é triangular.')
n1, n2, n3 = 1, 2, 3
num = int(input('Digite o número: '))
while(n1*n2*n3 < num):
    n1, n2, n3 = n2, n3, n3+1
if(n1*n2*n3 == num):
    print(f'O número {num} é triângular.')
else:
    print(f'O número {num} não é triângular.')
