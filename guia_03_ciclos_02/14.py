print('Suma de N factorial')

numero_ingresado = int(input('Ingrese un número: '))
numero = numero_ingresado
factorial = 1
suma = 0

while numero > 0:
    for i in range (1, numero+1):
        factorial = factorial * i
        print(f'factorial {i} = {factorial}')
        numero = numero - 1
        suma = suma + factorial
print (f'La suma de los primeros {numero_ingresado} factoriales es {suma}.')