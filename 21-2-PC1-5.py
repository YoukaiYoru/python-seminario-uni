"""
Escriba un programa que pida el radio y las cordenadas del
centro de una circunferencia y las coordenadas de un punto y que indique si el punto está
sobre la circunferencia, dentro o fuera de ella.

"""
#Pidiendo centro de circunferencia
circunferencia_x = float(input("Ingrese la coordenada X del centro: "))
circunferencia_y = float(input("Ingrese la coordenada Y del centro: "))


#Pidiendo radio de circunferencia
radio = float(input("Ingrese el radio de una circunferencia: "))




#Pidiendo cordenadas
x = float(input("Ingrese una coordenada a evaluar en eje X: "));
y = float(input("Ingrese una coordenada a evaluar en eje Y: "));

#Calculando distancia entre puntos
distancia = float(((x-circunferencia_x)**2+(y-circunferencia_y)**2)**(1/2))

#Saber si está dentro o fuera de la circunferencia

if (distancia<radio):
   print("El punto está DENTRO de la circunferencia")
else:
   if(distancia==radio):
      print("el punto se encuentra SOBRE la circunferencia")
   else:
      print("El punto se encuentra FUERA de la circunferencia")