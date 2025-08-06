print("\nCiclo while: Teclea la calificación del 0 al 100 (numero negativo para salir)")
cal=0
suma=0
cont=0
while cal >= 0:
    cal = int(input("Teclea una calificación: "))
    if cal>0:
        suma=suma + cal
    cont=cont + 1
promedio=suma/cont 
print("Calificaciones ingresadas", cont)   
print ("El promedio es", promedio)
print("Terminaste el ciclo.")