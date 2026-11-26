salario = float (input ("Qual valor fixo do salario:"))
vendas = float (input ("Valor de vendas feitas pelo colaborador:"))
comissao = vendas * 4 / 100
valorfinal = comissao + salario
 
print (f"Valor de comissão : R$ {comissao}, totalizando junto ao pagamento R${valorfinal}.")
