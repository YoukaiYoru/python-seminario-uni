"""

Implemente un algoritmo que permita calcular el  valor
de la expresión S para un valor determinado de n dado como dato.

S:
   S1 => para valores impares de n
   S2 => para valores pares de n

   S1 = (Sumatoria) i hasta n => i**4+  6i**3 + 5
   S2 = (Sumatoria) i hasta n => i**5+  (3i**3)/20 + 5


"""
#Definiendo funciones para los casos de S

def s1(numero):
   resultado=int(numero**4 + 6*(numero**3)+5)

   return resultado

def s2(numero):
   resultado= int(numero**5+(numero**3)+5)

   return resultado

#Valor de n

n = int(input("Ingrese un numero: "))

#Variables auxiliares

sumatoria1 = 0
sumatoria2 = 0

#Lógica del código

if((n%2)!=0):
   for k in range(n+1):
      sumatoria1=sumatoria1+s1(k)
   print("El valor de S es ",sumatoria1)
else:
   for j in range (n+1):
      sumatoria2=sumatoria2+s2(j)
   print("El valor de S es ",sumatoria2)

