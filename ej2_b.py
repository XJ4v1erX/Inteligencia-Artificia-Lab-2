import random

def lanzar_dados():
    D1 = random.randint(1, 6)
    D2 = random.randint(1, 6)
    return D1, D2

N = 10000  # Número de experimentos
sumas = []

for _ in range(N):
    D1, D2 = lanzar_dados()
    sumas.append(D1 + D2)

promedio = sum(sumas) / N
print(f"El promedio de las sumas es: {promedio}")