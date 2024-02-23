print("Vertice 1 [A]:")
x1 = float(input("\tCoordenada x: "))
y1 = float(input("\tCoordenada y: "))
print("Vertice 2 [B]:")
x2 = float(input("\tCoordenada x: "))
y2 = float(input("\tCoordenada y: "))
print("Vertice 3 [C]:")
x3 = float(input("\tCoordenada x: "))
y3 = float(input("\tCoordenada y: "))
print("Punto arbitrario [P]:")
xx = float(input("\tCoordenada x: "))
yy = float(input("\tCoordenada y: "))

posicion = "fuera"

PAxPB = ((x1-xx)*(y2-yy))-((x2-xx)*(y1-yy))
PBxPC = ((x2-xx)*(y3-yy))-((x3-xx)*(y2-yy))
PCxPA = ((x3-xx)*(y1-yy))-((x1-xx)*(y3-yy))

if ((PAxPB >= 0 and PBxPC >= 0 and PCxPA >= 0) or (PAxPB <= 0 and PBxPC <= 0 and PCxPA <= 0)):
    posicion = "dentro"

print(f"El punto P se encuentra {posicion} del triángulo ABC")
