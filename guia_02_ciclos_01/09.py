numero = int(input('Ingrese un número: '))
factorial = 1

for i in range(numero):
    factorial = factorial * (i+1)
print(factorial)