import random

def ini_pop(size, length):
    return [[random.choice([0, 1]) for _ in range(length)] for _ in range(size)]

def affinity(ab):
    return sum(ab)

def best(pop, n):
    return sorted(pop, key=affinity, reverse=True)[:n]

def mutate(pop, rate):
    for ab in pop:
        for i in range(len(ab)):
            if random.random() < rate:
                ab[i] ^= 1
    return pop

def clonal_algo(size, length, clones, rate, gens):
    pop = ini_pop(size, length)
    for _ in range(gens):
        pop += mutate(best(pop, clones), rate)
    for ab in pop:
        print(ab, '->', affinity(ab))
    return max(pop, key=affinity)

best_ab = clonal_algo(50, 10, 10, 0.1, 50)
print("Best antibody", best_ab)