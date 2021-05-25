print('Primeras 4 potencias de 2 de 3 maneras distintas')

print('Forma 1')

for i in range(1, 5):
    potencia = 2**i
    print(potencia, end = ' ')

print('\nForma 2')

potencia_2 = 1
for i in range(4):
    potencia_2 = potencia_2 * 2
    print(potencia_2, end = ' ')

print('\nForma 3')

potencia_3 = 1
while potencia_3 <= 4:
    calculo = 2**potencia_3
    potencia_3 = potencia_3 + 1
    print(calculo, end = ' ') 