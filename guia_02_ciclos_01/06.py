numero_ingresado = int(input('Ingrese un número, programa finaliza con un -1: '))
suma = 0

while numero_ingresado != -1:
    suma  = suma + numero_ingresado
    numero_ingresado = int(input('Ingrese un número, programa finaliza con un -1: '))

if numero_ingresado == -1:
    print('Programa finalizado')
    print(f'Suma total: {suma}')