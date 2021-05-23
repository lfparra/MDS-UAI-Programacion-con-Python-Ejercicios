numero_empleados = int(input('Ingrese el número de empleados de su empresa: '))

for i in range(numero_empleados):
    nombre_empleado = input(f'Ingrese nombre de empleado N° {i+1}: ')
    horas_semanales = int(input(f'Ingrese el número de horas semanales trabajadas por {nombre_empleado}: '))
    valor_hora_trabajada = int(input(f'Ingrese valor de la hora trabajada de {nombre_empleado}: '))
    salario = horas_semanales*valor_hora_trabajada
    print(f'El salario de {nombre_empleado} es de ${salario} por {horas_semanales} horas semanales a ${valor_hora_trabajada} la hora.')