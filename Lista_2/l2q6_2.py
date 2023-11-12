salario_por_hora = float(input('Quanto você recebe por hora? Resposta: '))
horas_trabalhadas = float(input('Quantas horas você trabalhou no mês? Resposta: '))

salario_bruto = salario_por_hora * horas_trabalhadas

ir = (salario_bruto * 0.11)

inss = (salario_bruto * 0.08)

sindicato = (salario_bruto * 0.05)

salario_liquido = salario_bruto - ir - inss - sindicato

print(f'O salário bruto foi {salario_bruto} reais, pagou para o INSS {inss} reais, pagou para o sindicato {sindicato} reais e recebeu {salario_liquido} reais.')

