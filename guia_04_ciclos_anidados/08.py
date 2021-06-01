numero = int(input('Ingresa un número entero positivo: '))
contador = 1
for i in range(1, numero+1):
    for j in range(i):
        print(contador, end =' ')
        contador = contador + 1
    print(' ')
