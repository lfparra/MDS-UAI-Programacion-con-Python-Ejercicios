print('Menor número ingresado. Programa finaliza con 0')

numero_ingresado = int(input('Ingresa un número: '))
menor_numero = numero_ingresado

while numero_ingresado != 0:
    if numero_ingresado < menor_numero:
        menor_numero = numero_ingresado
    numero_ingresado = int(input('Ingresa un número: '))

print(f'El menor número ingresado es {menor_numero}.')

