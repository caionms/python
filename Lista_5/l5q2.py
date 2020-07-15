print('Iremos ajudar Daniela a descobrir quantos números sortudos existem entre 18644 e 33087.')
count = 0
for num in range(18644, 33087):
    teste = str(num)
    if "7" not in teste:
        if "2" in teste:
            count += 1
print(f'Existem {count} números sortudos no intervalo.')
