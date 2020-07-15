print('Iremos calcular quantos digitos existem em um número.')
num = str(input('Digite um número ou digite 0 para padrão: '))
if num == '0':
    num = str(2**1000000)
print(f'Existem {len(num)} digitos.')
