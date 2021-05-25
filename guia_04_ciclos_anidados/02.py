escalones = int(input('Ingresa el número de escalones: '))


filas = escalones * 2
pisos = escalones
contador = 0

for i in range(filas):
    for j in range(pisos):
        print('#', end ='')
        
    contador = contador + 1

    if contador == 2:
        contador = 0
        pisos = pisos - 1

    print('')
