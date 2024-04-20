import numpy as np
import matplotlib.pyplot as plt

def simulate_dice_rolls(N):
    results = []
    for _ in range(N):
        count = 1
        while True:
            roll = np.random.randint(1, 7)
            if roll in {2, 3, 4, 5}:
                results.append(count)
                break
            count += 1
    return results

results_10 = simulate_dice_rolls(10)
results_100 = simulate_dice_rolls(100)
results_1000 = simulate_dice_rolls(1000)
results_10000 = simulate_dice_rolls(10000)

def plot_results(results, N):
    plt.figure(figsize=(10, 6))
    plt.hist(results, bins=range(1, max(results) + 2), align='left', density=True, alpha=0.75, label=f'N = {N}')
    plt.xlabel('Numero de lanzamientos')
    plt.ylabel('Probabilidad')
    plt.title(f'Distribucion de lanzamientos para N = {N}')
    plt.xticks(range(1, max(results) + 1))
    plt.legend()
    plt.grid(True)
    plt.show()

plot_results(results_10, 10)
plot_results(results_100, 100)
plot_results(results_1000, 1000)
plot_results(results_10000, 10000)
