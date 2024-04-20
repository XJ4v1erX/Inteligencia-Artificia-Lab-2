import numpy as np

p = 0.3  

adj_matrix = np.zeros((10, 10))

adj_matrix[0, 1] = adj_matrix[0, 2] = 1 - p 
adj_matrix[1, 2] = adj_matrix[1, 3] = 1 - p  
adj_matrix[2, 3] = 1 - p  
adj_matrix[3, 4] = adj_matrix[3, 6] = 1 - p  
adj_matrix[4, 5] = adj_matrix[4, 7] = 1 - p  
adj_matrix[5, 6] = 1 - p  
adj_matrix[6, 9] = 1 - p  
adj_matrix[7, 8] = adj_matrix[7, 9] = 1 - p 
adj_matrix[8, 9] = 1 - p  


adj_matrix = adj_matrix + adj_matrix.T

paths = [
    (0, 1, 3, 4, 5, 6, 9),  # A -> B -> D -> E -> F -> G -> J
    (0, 1, 3, 6, 9),        # A -> B -> D -> G -> J
    (0, 2, 3, 4, 5, 6, 9),  # A -> C -> D -> E -> F -> G -> J
    (0, 2, 3, 6, 9),        # A -> C -> D -> G -> J
    (0, 1, 3, 4, 7, 8, 9),  # A -> B -> D -> E -> H -> I -> J
    (0, 1, 3, 4, 7, 9),     # A -> B -> D -> E -> H -> J
    (0, 2, 3, 4, 7, 8, 9),  # A -> C -> D -> E -> H -> I -> J
    (0, 2, 3, 4, 7, 9)      # A -> C -> D -> E -> H -> J
]


total_probability = 0
for path in paths:
    path_probability = 1
    for i in range(len(path) - 1):
        path_probability *= adj_matrix[path[i], path[i+1]]
    total_probability += path_probability




transition_matrix = np.zeros_like(adj_matrix)

for i in range(len(adj_matrix)):
    row_sum = np.sum(adj_matrix[i])
    if row_sum > 0:
        transition_matrix[i] = adj_matrix[i] / row_sum


def simulate_walk(transition_matrix, start_node, end_node, max_steps=1000):
    current_node = start_node
    steps = 0
    

    while current_node != end_node and steps < max_steps:
        steps += 1
        current_node = np.random.choice(np.arange(len(transition_matrix)), p=transition_matrix[current_node])
    
    return steps if current_node == end_node else None

num_experiments = 10000  
steps_to_end = []


for _ in range(num_experiments):
    result = simulate_walk(transition_matrix, start_node=0, end_node=9)
    if result is not None:
        steps_to_end.append(result)



M = 100
N = 10000

def simulate_markov_chain(transition_matrix, num_movements, start_node=0):
    current_node = start_node
    node_positions = np.zeros(len(transition_matrix))
    

    for _ in range(num_movements):
        current_node = np.random.choice(np.arange(len(transition_matrix)), p=transition_matrix[current_node])
        node_positions[current_node] += 1
    
    node_distribution = node_positions / num_movements
    return node_distribution

aggregate_distribution = np.zeros(len(transition_matrix))
for _ in range(N):
    aggregate_distribution += simulate_markov_chain(transition_matrix, M)

steady_state_distribution = aggregate_distribution / N
steady_state_distribution

total_probability
steps_distribution = np.bincount(steps_to_end) / len(steps_to_end)

steps_distribution, np.mean(steps_to_end)
