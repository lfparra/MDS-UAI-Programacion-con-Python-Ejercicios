print('Primeros N números primos')
numero = int(input('Ingresa un número: '))
for i in range(2, numero+1):
    contador = 0
    for j in range(1, i+1):
        if i%j == 0:
            contador = contador + 1
            #print(i, j)
    if contador == 2:
        print(i, end = ' ')