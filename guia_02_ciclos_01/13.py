print('Ingresa un número para saber si es un número primo')
numero = int(input('Ingresa un número entero y positivo: '))
contador = 0

while contador < 2:
    for i in range (1, numero+1):
        if numero % i == 0:
            contador = contador + 1

if contador == 2:
    print(f'El número {numero} es primo.')
else: 
    print(f'El número {numero} no es primo.')        

