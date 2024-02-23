"""
Crear un programa que reciba un número entero positivo N (N>1000)
Luego presente el número modificado de tal forma que se ha eliminado 
de dicho número el menor dígito

"""
# Encontrar el menor dígito
def menor_digito(numero):
   min_digito = 9
   while numero > 0:
      digito = numero % 10
      if digito < min_digito:
            min_digito = digito
      numero //= 10
   return min_digito


#Haciendo una función que elimine el menor dígito
def eliminar_menor(numero):
   if numero < 10:
   # Si el número tiene un solo dígito, no hay nada que eliminar
      return 0

   # Inicializar variables
   nuevo_numero = 0
   multiplicador = 1
   copia_numero = numero

   min_digito = menor_digito(numero)
   # Construir un nuevo número sin el menor dígito
   numero = copia_numero  # Restaurar el valor original del número
   while numero > 0:
      digito = numero % 10
      if digito != min_digito:
         nuevo_numero += digito * multiplicador
         multiplicador *= 10
      numero //= 10

   return nuevo_numero

numero = int(input("Ingrese un número mayor a 1000: "))

if numero<1000:
   print("EL número no es mayor a 1000. Ejecute de nuevo.")
else:
   print("Se ha ingresado: ",numero)
   menorDigito = menor_digito(numero)
   print("El menor digito es: ",menorDigito)
   nuevo_numero= eliminar_menor(numero)
   print("El nuevo numero es ", nuevo_numero)



#Comentario de Edward: También se puede hacer con arrays o string me parece y sale más rápido
#Pero me parece que para pc1 aún no ven eso.