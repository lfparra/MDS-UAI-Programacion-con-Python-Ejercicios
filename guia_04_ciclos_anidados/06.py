print('Suma de los primeros N factoriales')
numero = int(input('Numero: '))
suma_factorial = 0

for i in range(1, numero+1):
    #print(i)
    factorial = 1
    for j in range(1, i+1):
        factorial = j*factorial
    suma_factorial = suma_factorial + factorial    
print(f'La suma de los primeros {numero} factoriales es {suma_factorial}.')

