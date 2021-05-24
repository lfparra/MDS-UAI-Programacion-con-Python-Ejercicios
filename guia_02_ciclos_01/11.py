print('Empecemos el juego')
print('Tienes cuatro tipos de fichas para jugar')
print('Ficha "a" - Ficha "b" - Ficha "c" - Ficha "d"')
print('Finaliza el juego aprentando "n"')

ficha = input('Ingresa tu ficha: ')
posicion = 1

while ficha != 'n':
    if ficha == 'a' or ficha == 'b' or ficha == 'c' or ficha == 'd':
        if posicion == 1:
            if ficha == 'a':
                posicion = 2
        elif posicion == 2:
            if ficha == 'b':
                posicion = 1
            elif ficha == 'c':
                posicion = 4
        elif posicion == 3:
            if ficha == 'a':
                posicion = 1
            elif ficha == 'b':
                posicion = 4
        else:
            if ficha == 'd':
                posicion = 3
        ficha = input('Ingresa una nueva ficha: ')
    else:
        print('Ficha incorrecta, ingresa nuevamente')
        ficha = input('Ingresa tu ficha: ')

if posicion == 4:
    print(f'Ganaste!!! Llegaste a la posición N° {posicion}.')
else:
    print(f'Perdiste!! No pudiste llegar a la posición N° 4, sólo llegaste a la posición N° {posicion}.')
    