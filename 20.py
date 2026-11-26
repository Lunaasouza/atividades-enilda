ano = int (input ("Digite o ano para saber se é bissexto"))

if ano % 400 == 0 :
    print ("É bissexto")
elif ano % 100 == 0 :
    print ("não é bissexto")
elif ano % 4 == 0 :
    print ("é bissexto")
else :
    print ("não é bissexto")
    