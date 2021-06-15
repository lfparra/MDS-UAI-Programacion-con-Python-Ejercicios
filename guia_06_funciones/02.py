def pedir_dato():
    numero = input('Ingrese un número entre 1 y 100, abos inclusive: ')
    while numero.isdigit() == False or int(numero) < 1 or int(numero) > 100:
        if numero.isdigit() == False:
            numero = input('Error en tipo de dato! Ingrese nuevamente un número entre 1 y 100, aMbos inclusive: ')
        elif int(numero) < 1 or int(numero) > 100:
            numero = input('Fuera de rango! Ingrese nuevamente un número entre 1 y 100, aMbos inclusive: ')

    return int(numero)

valor = pedir_dato()

if(valor%2==0):
    print("Numero par")
else:
    print("Numero impar")