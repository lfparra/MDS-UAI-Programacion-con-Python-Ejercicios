print('Ingrese los valores a, b y c de una ecuación cuadrática')
a = int(input('Ingresa a: '))
b = int(input('Ingresa b: '))
c = int(input('Ingresa c: '))

discriminativo = b**2 - 4*a*c
print(f'Discriminativo = {discriminativo}')

if discriminativo < 0:
    print('No hay soluciones reales')
elif discriminativo == 0:
    x1 = -b + (discriminativo**0.5)/(2*a)
    print(f'Hay una solución real y es x1 = {round(x1, 2)}')
else:
    x1 = -b + (discriminativo**0.5)/(2*a)
    x2 = -b - (discriminativo**0.5)/(2*a)
    print(f'Hay dos soluciones reales y son x1 = {round(x1, 2)} y x2 = {round(x2, 2)}')


