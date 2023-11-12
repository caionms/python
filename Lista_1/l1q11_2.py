def calcula_valor(valor):
    return len(str(valor))
    
def run():
    potencia = int(input("Qual valor você quer elevar 2? Valor:"))
    print(f'A quantidade de digitos de 2 elevado a {potencia} eh igual a {calcula_valor(2**potencia)}!')
    
run()
