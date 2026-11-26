lado1 = float (input ("Valor do primeiro lado"))
lado2 = float (input ("Valor do segundo lado"))
lado3 = float (input ("Valor do terceiro lado"))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
  forma = ("Você formou um triangulo")
else:
  forma = ("Você não formou um triangulo")
  
  print (forma)
  
if   lado1 == lado2 and lado2 == lado3:
        print("Triângulo equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Triângulo isósceles.")
else:
        print("Triângulo escaleno.")
        
        