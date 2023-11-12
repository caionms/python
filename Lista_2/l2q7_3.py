metros_q = int(input('Digite a quantidade de metros quadrados da area a ser pintada: '))

quantidade_de_litros = metros_q/3

quantidade_de_latas = int(quantidade_de_litros/18)

if quantidade_de_litros%18 > 0.0:
    quantidade_de_latas = quantidade_de_latas + 1

print(f'Vai ser necessário comprar {quantidade_de_latas} latas, que vão custar {quantidade_de_latas * 80} reais!')
