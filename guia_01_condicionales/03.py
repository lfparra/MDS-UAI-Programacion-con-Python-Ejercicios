A = int(input('Ingresa A: '))
B = int(input('Ingresa B: '))

division = A%B

if division == 0:
    print('B divide exactamente a A')
else:
    print('B no divide a A en forma entera')