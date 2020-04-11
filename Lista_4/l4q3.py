import random
print('Iremos gerar dois vetores de 10 elementos e intercalar eles.')
l1 = []
l2 = []
lc = []
for x in range(10):
    l1.append(random.randrange(1,100))
l1.sort()
aux1 = l1.copy()
for y in range(10):
    l2.append(random.randrange(1,100))
l2.sort()
aux2 = l2.copy()
while(len(aux1) > 0 and len(aux2) > 0):
    if(aux1[0] > aux2[0]):
        lc.append(aux2[0])
        aux2.remove(aux2[0])
    else:
        lc.append(aux1[0])
        aux1.remove(aux1[0])
print(f'A primeira lista é {l1}.\nA segunda lista é {l2}.\nO resultado da intercalação é {lc}.')
    
