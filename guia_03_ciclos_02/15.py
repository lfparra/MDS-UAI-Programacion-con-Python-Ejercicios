print('Número palíndrome')

numero = input('Ingrese un numero: ')
comparación = ''


for i in range(len(numero)-1, -1, -1):
   comparación = comparación + numero[i]
   print(comparación)

if numero == comparación:
    print(f'El número ingresado {numero} es palíndromo.')

else:
    print(f'El número ingresado {numero} no es palíndromo.')
