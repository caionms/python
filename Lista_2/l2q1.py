print('Iremos identificar se o triângulo é equilátero, isósceles ou escaleno de acordo com seus lados!')
l1 = int(input('Insira o primeiro lado: '))
l2 = int(input('Insira o segundo lado: '))
l3 = int(input('Insira o terceiro lado: '))
if((l1 + l2) > l3 or (l1 + l3) > l2 or (l2 + l3) > l1):
    if(l1 == l2 and l2 == l3):
        print('O triângulo é equilátero!')
    elif(l1 == l2 or l2 == l3 or l1 == l3):
        print('O triângulo é isósceles!')
    elif(l1 != l2 and l2 != l3):
        print('O triângulo é escaleno!')
else:
    print('Os valores são inválidos, não é possível formar um triângulo!')

   
