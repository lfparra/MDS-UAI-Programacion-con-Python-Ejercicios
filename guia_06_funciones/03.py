def tipo_triangulo(lado_1, lado_2, lado_3):
    if lado_1 == lado_2 == lado_3:
        return 2
    elif lado_1 != lado_2 and lado_2 != lado_3 and lado_1 != lado_3:
        return 0
    else:
        return 1

triangulos = []
equilatero = 0
escaleno = 0
isosceles = 0

numero_triangulos = int(input('Ingrese el número de triángulo: '))

for i in range(numero_triangulos):
    print(f'Triangulo {i+1}')
    lado_1 = int(input('Ingrese lado 1: '))
    lado_2 = int(input('Ingrese lado 2: '))
    lado_3 = int(input('Ingrese lado 3: '))
    print(f'Triángulo tipo: {tipo_triangulo(lado_1, lado_2, lado_3)}')

    if tipo_triangulo(lado_1, lado_2, lado_3) == 2:
        equilatero = equilatero + 1
    elif tipo_triangulo(lado_1, lado_2, lado_3) == 0:
        escaleno = escaleno + 1
    else:
        isosceles = isosceles + 1

print(f'Se ingresaron {equilatero} triángulos equilateros, {isosceles} triángulos isósceles y {escaleno} triángulos escalenos.')








