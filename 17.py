salario = float(input("Qual seu salario atual: "))

if salario <= 280:
    percentual = 20
    aumento = salario * 20 / 100
elif salario <= 700:
    percentual = 15
    aumento = salario * 15 / 100
elif salario <= 1500:
    percentual = 10
    aumento = salario * 10 / 100
else:
    percentual = 5
    aumento = salario * 5 / 100

novo_salario = salario + aumento

print(f"Salário antes do reajuste: R$ {salario:.2f}")
print(f"Percentual de aumento aplicado: {percentual}%")
print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")