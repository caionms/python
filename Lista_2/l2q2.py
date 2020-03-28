import calendar
print('Iremos conferir se um ano é bissexto!')
ano = int(input('Digite um ano: '))
if(calendar.isleap(ano)):
    print('O ano é bissexto!')
else:
    print('O ano não é bissexto!')
