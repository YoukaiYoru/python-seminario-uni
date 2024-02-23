flag = True
while(flag):
    n = int(input("Inserte un número entero (mayor que 3): "))
    if(n > 3):
        flag = False

txt_operacion = f'n = {n}\n'
suma = 0
sumando = 1
while(sumando <= n):
    factor = sumando
    factorial = 1
    while(factor > 0):
        factorial *= factor
        factor -= 1
    suma += factorial
    if(sumando == n):
        txt_operacion += f'{sumando}! = {suma}'
    else:
        txt_operacion += f'{sumando}! + '
    sumando += 1

print(txt_operacion)

