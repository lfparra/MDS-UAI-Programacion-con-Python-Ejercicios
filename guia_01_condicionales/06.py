print('Veremos que fecha ocurre primero')

print('Ingrese día, mes y año de la primera fecha en números')

fecha_1_dia = int(input('Día: '))
fecha_1_mes = int(input('Mes (en números): '))
fecha_1_año = int(input('Año: '))

print('Ingrese día, mes y año de la segunda fecha en números')

fecha_2_dia = int(input('Día: '))
fecha_2_mes = int(input('Mes (en números): '))
fecha_2_año = int(input('Año: '))

#Ambos años iguales
if fecha_1_año == fecha_2_año:

    #Ambos meses iguales
    if fecha_1_mes == fecha_2_mes:

        #Ambos días iguales
        if fecha_1_dia == fecha_2_dia:
            print(f'Ambas fechas son iguales al {fecha_1_dia}-{fecha_1_mes}-{fecha_1_año}')

        #Día fecha 1 anterior a día año 2
        elif fecha_1_dia < fecha_2_dia :
            print(f'La primera fecha del {fecha_1_dia}-{fecha_1_mes}-{fecha_1_año} ocurre antes que la segunda fecha del {fecha_2_dia}-{fecha_2_mes}-{fecha_2_año}')
        
        #Día fecha 2 anterior a día año 1
        else:
            print(f'La segunda fecha del {fecha_2_dia}-{fecha_2_mes}-{fecha_2_año} ocurre antes que la primera fecha del {fecha_1_dia}-{fecha_1_mes}-{fecha_1_año}')

    #Mes fecha 1 anterior a mes fecha 2
    elif fecha_1_mes < fecha_2_mes:
        print(f'La primera fecha del {fecha_1_dia}-{fecha_1_mes}-{fecha_1_año} ocurre antes que la segunda fecha del {fecha_2_dia}-{fecha_2_mes}-{fecha_2_año}')

    #Mes fecha 2 anterior a mes fecha 1
    else:
       print(f'La segunda fecha del {fecha_2_dia}-{fecha_2_mes}-{fecha_2_año} ocurre antes que la primera fecha del {fecha_1_dia}-{fecha_1_mes}-{fecha_1_año}')

#Año fecha 1 anterior a año fecha 2
elif fecha_1_año < fecha_2_año:
   print(f'La primera fecha del {fecha_1_dia}-{fecha_1_mes}-{fecha_1_año} ocurre antes que la segunda fecha del {fecha_2_dia}-{fecha_2_mes}-{fecha_2_año}')

#Año fecha 2 anterior a año fecha 1
else:
   print(f'La segunda fecha del {fecha_2_dia}-{fecha_2_mes}-{fecha_2_año} ocurre antes que la primera fecha del {fecha_1_dia}-{fecha_1_mes}-{fecha_1_año}')
