print('Ingresa el estado de los 7 puentes (0: no operativo - 1: operativo)')

puente_1 = int(input('Estado Puente 1: '))
puente_2 = int(input('Estado Puente 2: '))
puente_3 = int(input('Estado Puente 3: '))
puente_4 = int(input('Estado Puente 4: '))
puente_5 = int(input('Estado Puente 5: '))
puente_6 = int(input('Estado Puente 6: '))
puente_7 = int(input('Estado Puente 7: '))

if puente_2 == 1 or puente_1 == 1 and puente_4 == 1 or puente_3 == 1 and puente_5 == 1:
    if puente_6 == 1 or puente_7 == 1:
        print('Pudiste pasar desde la isla A a la isla B')
    else:
        print('No pudiste pasar desde la isla A a la isla B')
else:
    print('No pudiste pasar desde la isla A a la isla B')