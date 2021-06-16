def es_primo(num):
    count = 0
    for i in range(2, num+1):
        if num % i == 0:
            count = count + 1
    if count > 1:
        return 0
    else:
        return 1

numero_ingresado = 20

for i in range(2, numero_ingresado+1):
    #print(f'i = {i}')
    if es_primo(i) == 1:
        print(f'Es primo: {i}')
    
    