num = float (input ("Digite um numero para verificar se é positivo ou negativo: "))

if num > 0 :
 tipo = "positivo"
elif num == 0 :
    tipo = "neutro"
else:
    tipo = "negativo" 
    


print(f"O numero digitado : {num} é um numero {tipo}") 