"""
Realizar un programa que permita obtener los divisores de un número

"""

#Pidiendo número al usuario

numero = int(input("Ingrese un número entero a evaluar: "))

#Encontrando divisores

for i in range(1,numero+1):
   if((numero % i)==0):
      print(i," es divisor")