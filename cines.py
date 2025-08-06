edad=int (input("Dame la edad"))
if edad>=0 and edad<=4:
    print ("entrada gratis")
elif edad>=4 and edad <=12:
    print ("Boleto infantil de $40")
elif edad >=13 and edad <=59:
    print ("Boleto general de $70")
elif edad>=60:
   print ("Boleto de adulto mayor con descuento de $35") 
else:
    print ("Edad no válida")