import numpy as np

def dos_dimensiones(num_1, num_2):
    array = np.zeros((num_1, num_2))
    #print(array)
    #print('')
    for i in range(1, num_1+1):
        for j in range(1, num_2+1):
            array[i-1][j-1] = i*j
    print(array)
    return

dos_dimensiones(5, 3)
