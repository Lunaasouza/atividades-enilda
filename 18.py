valor_hora = float (input ("Qual valor hora:"))
horas_mes = float (input ("qual quantidade de horas trabalhadas:"))

salario_bruto = valor_hora * horas_mes

inss = salario_bruto * 10 /100
sidicato = salario_bruto * 3/100 
fgts = salario_bruto * 11 / 100

if salario_bruto <= 900 :
    valorir = 0
elif salario_bruto <= 1500 :
    valorir = salario_bruto * 5 /100
elif salario_bruto <= 2500:
   valorir = salario_bruto * 10/100 
else:
    valorir = salario_bruto * 20/100


total_descontos =valorir + inss + sidicato

salario_liquido = salario_bruto - total_descontos

print (f"Salário bruto: R${salario_bruto}:.2f")
print (f"(-) IR: R$ {valorir: 2f}")
print (f"(-)INSS (10%): R$ {inss:.2F}") 
print(f"(-) Sindicato (3%): R$ {sidicato:.2f}")
print(f"FGTS (11%): R$ {fgts:.2f}")
print(f"Total de descontos: R$ {total_descontos:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")



