print('10 primeros números pares de 3 formas distintas')

print('Forma 1')

for i in range(2, 21, 2):
    print(i, end = ' ')


print('\nForma 2')
for j in range(2, 21):
    if j % 2 == 0:
        
        print(j, end = ' ')

contador = 1

print('\nForma 3')
while contador < 21:
    if contador % 2 == 0:
        print(contador, end = ' ')
    contador = contador + 1