def edad(anio):
    print(f'Este año cumples {2021-anio} años.')
    return

print("¿En qué año naciste?")
anio=int(input())
edad(anio)



def edad_2(anio):
    return 2021-anio

print("¿En qué año naciste?")
anio_2=int(input())
print(f'Este año cumples {edad_2(anio_2)} años.')