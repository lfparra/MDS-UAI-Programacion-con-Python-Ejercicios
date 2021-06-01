print('Ingresar valor inferior y superior de x para f(x)')

valor_inferior = int(input('Ingrese el valor inferior de x: '))
valor_superior = int(input('Ingrese el valor superior de x: '))

for i in range(valor_inferior, valor_superior+1):
    suma = 0
    for j in range(1, i+1):
        suma = suma + (j*j)
    print(f'x = {i} => f(x) = {suma}')