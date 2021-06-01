print('Ingrese su genero')
print('Para genero femenino ingrese "f"')
print('Para genero masculino ingrese "m"')
print('Si prefiere no informarlo ingrese "n"')
print('Programa finaliza ingresando "x"')
genero = input()
personas_ingresadas = 0
suma_f = 0
suma_m = 0
suma_n = 0

while genero != 'x':
    personas_ingresadas = personas_ingresadas + 1

    if genero == 'f':
        suma_f = suma_f + 1

    elif genero == 'm':
        suma_m = suma_m + 1

    else:
        suma_n = suma_n + 1

    genero = input('Ingrese datos de genero de la siguiente persona: ')

porcentaje_f = round(suma_f/personas_ingresadas*100, 2)
porcentaje_m = round(suma_m/personas_ingresadas*100, 2)
porcentaje_n = round(suma_n/personas_ingresadas*100, 2)

print(f'Se registraron {personas_ingresadas} personas, de las cuales el {porcentaje_f}% son mujeres, el {porcentaje_m}% son hombres y el {porcentaje_n}% no entregó información.')
