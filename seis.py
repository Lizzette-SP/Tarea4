import numpy as np

def arreglo():
    arr = np.zeros((10, 10, 10), dtype=int)

    i, j, k = np.indices((10, 10, 10))

    mascara_i = i % 2 == 1
    
    mascara_j = j % 2 == 0
    
    mascara_k = np.isin(k, [2, 3, 5, 7])
    
    mascara = mascara_i & mascara_j & mascara_k
 
    arr[mascara] = 1

    ones_positions = np.argwhere(arr == 1)
    print(ones_positions[:10])

    return arr

array = arreglo()
print("Número de elementos con valor 1:", np.sum(array))
