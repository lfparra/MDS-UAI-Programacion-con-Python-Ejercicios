escalones = int(input('Ingresa el número de escalones: '))
filas = escalones
pisos = (escalones*2) - (escalones*2-2)

for i in range(filas):
    for j in range(pisos):
        print('#', end ='')
    pisos = pisos + 2

    print('')