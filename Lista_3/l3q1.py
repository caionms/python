nota = int(input('Digite uma nota: '))
if(nota >= 0 and nota <= 10):
    print('Valor válido!')
else:
    while(nota < 0 or nota > 10):
        print('Valor inválido!')
        nota = int(input('Digite uma nota: '))
        if(nota >= 0 and nota <= 10):
            print('Valor válido!')
