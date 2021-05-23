clave_ingresada = int(input('Ingrese la clave de su tarjeta: '))

clave_registrada = 1234
intentos = 3
condicion = True

while condicion:
    intentos = intentos - 1
    if clave_ingresada == clave_registrada:
        print('Bienvenido al Servicio')
        condicion = False
    else:
        if intentos <= 0:
            print('Tres intentos incorrectos, Tarjeta bloqueada!!!')
            condicion = False
        else:
            print(f'Clave incorrecta, le quedan {intentos} intento(s)')
            clave_ingresada = int(input('Ingrese la clave de su tarjeta: '))
