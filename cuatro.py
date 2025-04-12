import numpy as np

def remplazar_puntajes(puntajes):
    #Máscara para valores < 60
    mascara = puntajes < 60
    # índices de los primeros 3 True en la máscara
    first_three = np.where(mascara)[0][:3]

    result = puntajes.copy() #conservar el original
    
    result[first_three] = 0
    return result

# Generar datos de ejemplo
generator = np.random.default_rng(1010)

puntajes = np.round(generator.uniform(low=0, high=100, size=10))

print("Valores originales de las primeras 10 entregas:", puntajes)
print("Valores modificados de las primeras 10 entregas:", remplazar_puntajes(puntajes.copy()))