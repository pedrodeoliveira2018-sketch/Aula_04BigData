valor = float(input('qual foi seu valor gasto?'))
if valor >= 250:
   desconto =  0.16 * valor
   resultado = valor - desconto
   print(f'seu valor com desconto é de  {resultado} ') 
else:
    print (f'neste caso não a desconto {valor} ' )

    

