import matplotlib.pyplot as plt
import numpy as np
from ej2_b import lanzar_dados

def promedio_experimentos(M, N):
    promedios = []
    for _ in range(M):
        sumas = [sum(lanzar_dados()) for _ in range(N)]
        promedio = sum(sumas) / N
        promedios.append(promedio)
    return promedios

M_values = [5, 10, 50, 100, 200]
N = 10000

for M in M_values:
    promedios = promedio_experimentos(M, N)
    plt.hist(promedios, bins=20, density=True, alpha=0.7, label=f'M = {M}')

plt.xlabel('Promedio de las sumas')
plt.ylabel('Densidad')
plt.title('Distribución de los promedios')
plt.legend(loc='upper right')
plt.show()
