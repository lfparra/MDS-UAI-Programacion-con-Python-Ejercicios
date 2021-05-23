numero_A = int(input('Ingrese un número: '))
numero_B = int(input('Ingrese un segundo número: '))

diferencia = numero_A - numero_B
contador = abs(diferencia) + 1

while contador != 0:
    if diferencia < 0:
        print(numero_A)
        numero_A = numero_A + 1
    else:
        print(numero_A)
        numero_A = numero_A - 1
    
    contador = contador - 1