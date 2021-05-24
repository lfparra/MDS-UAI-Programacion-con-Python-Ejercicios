print('Ingresa un número para conocer los números primos que hay entre el 0 y este número')
numero = int(input('Ingresa un número entero y positivo: '))
contador = 0

for i in range(2, numero+1):
    for j in range(1, i+1):
        if i % j == 0:
            #print(i, j)
            contador = contador + 1
    #print(f'Contador de i={i} es {contador} ')
    if contador == 2:
        print(f'El número {i} es primo.')
    contador = 0