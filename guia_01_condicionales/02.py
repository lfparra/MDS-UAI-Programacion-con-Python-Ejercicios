prueba_1 = float(input('Resultado prueba 1: '))
prueba_2 = float(input('Resultado prueba 2: '))

promedio = (prueba_1 + prueba_2)/2

print(f'Tu promedio es {promedio}')

if promedio >= 4:
    print('Felicitaciones, vas camino a aprobar')
elif promedio < 3:
    print('Pocas posibilidades de aprobar')
else:
    print('Atención, vas camino a reprobar')

