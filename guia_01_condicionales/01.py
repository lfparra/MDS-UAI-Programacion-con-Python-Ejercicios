print("Ingresa tu edad:")
edad = int(input())
if (edad < 18):
    print("Acceso denegado")
else:
    if (edad < 25):
        print("Pase por caja 1")
    else:
        if (edad < 30):
            print("Pase por caja 2")
        else:
            print("Pase por caja 3")
