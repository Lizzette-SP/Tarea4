import numpy as np
def peces_vivos(locs, weights):
    #Posiciones como tuplas para usarlas como claves
    posiciones = [tuple(pos) for pos in locs]
    unicas = np.unique(posiciones, axis=0)
    
    # Para cada posición única, encontrar el pez más pesado
    sobrevivientes = []
    for pos in unicas:
        # Máscara para peces en esta posición
        mascara = (locs == pos).all(axis=1)
        # Índice del pez más pesado en esta posición
        max_idx = np.argmax(weights * mascara)
        sobrevivientes.append(max_idx)
    
    return np.sort(sobrevivientes)

# Generar pesos de peces entre 1 y 10
generator = np . random . default_rng (1010)
weights = generator . normal ( size =10)

# Posiciones fijas del ejercicio
locs = np.array([
    [0, 0, 0],
    [1, 1, 2],
    [0, 0, 0],
    [2, 1, 3],
    [5, 5, 4],
    [5, 0, 0],
    [5, 0, 0],
    [0, 0, 0],
    [2, 1, 3],
    [1, 3, 1]
])

print("Pesos de los peces generados:", weights)
print("Peces sobrevivientes:", peces_vivos(locs, weights))