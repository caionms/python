print('Iremos decompor um número em fatores primos.')
num = int(input('Digite o número: '))
lista = []
listaqtd = []
d = 2
while num > 1:
    if num % d == 0:
        listaqtd.append(d)
        if d not in lista:
            lista.append(d)
        num = num / d
    else:
        d += 1
print('Os fatores são: ')
for x in lista:
    print(f'    {x}^{listaqtd.count(x)}.')
