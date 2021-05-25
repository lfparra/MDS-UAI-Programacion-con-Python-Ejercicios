print('Primeros N números pares (de 2 maneras distintas)')

numero_ingresado = int(input('Ingrese un número entero y positivo: '))

print('Utilizando For Loop')
for i in range(2, (numero_ingresado*2)+1):
    if i % 2 == 0:
        print(i, end = ' ')


print('\nUtilizando While Loop')
contador = 1
while contador <= numero_ingresado*2:
    if contador % 2 == 0:
        print (contador, end = ' ')
    contador = contador + 1 