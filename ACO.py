import numpy as np
import matplotlib.pyplot as plt

cities = np.array([[0,0],[1,3],[3,1],[5,2],[6,6],[7,4],[8,8]])
n = len(cities)
dist = np.linalg.norm(cities[:,None] - cities, axis=2)

alpha = 1
beta = 2
rho = 0.5
Q = 100
n_ants = 10
n_iter = 100

pheromone = np.ones((n, n))
best_path = None
best_dist = float('inf')

def next_city(curr, visited):
    prob_numerator = (pheromone[curr][~visited] ** alpha) * (1 / dist[curr][~visited] ** beta)
    if prob_numerator.sum() == 0:
        return np.random.choice(np.where(~visited)[0])
    else:
        probabilities = prob_numerator / prob_numerator.sum()
        unvisited_indices = np.where(~visited)[0]
        return np.random.choice(unvisited_indices, p=probabilities)


for iteration in range(n_iter):
    pheromone *= (1 - rho)
    for ant in range(n_ants):
        start_city = np.random.randint(n)
        path = [start_city]
        visited = np.zeros(n, dtype=bool)
        visited[start_city] = True
        for step in range(n - 1):
            next_c = next_city(path[-1], visited)
            path.append(next_c)
            visited[next_c] = True
        path.append(path[0])
        total_distance = sum(dist[path[i]][path[i+1]] for i in range(n))
        if total_distance < best_dist:
            best_dist = total_distance
            best_path = path
        for i in range(n):
            pheromone[path[i]][path[i+1]] += Q / total_distance

print("Best path:", best_path)
print("Distance:", best_dist)
plt.plot(cities[best_path, 0], cities[best_path, 1], 'o-')
plt.title(f"Best Path - Distance: {best_dist:.2f}")
plt.show()
