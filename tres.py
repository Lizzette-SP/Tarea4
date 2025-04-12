import numpy as np

#Generar puntajes
generator = np.random.default_rng(1010)
love_scores = np.round(generator.uniform(low=0, high=100, size=10))

diferencias = np.abs(love_scores[:, np.newaxis] - love_scores)

print("Puntajes de amor generados:", love_scores)
print("\nMatriz de diferencias:")
print(diferencias)