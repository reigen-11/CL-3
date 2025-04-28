import random
from deap import base, creator, tools, algorithms

def eval_func(ind): 
    return sum(x**2 for x in ind)

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("attr_float", random.uniform, -5, 5)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=3)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("evaluate", eval_func)
toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

pop = toolbox.population(n=50)
for _ in range(20):
    offspring = algorithms.varAnd(pop, toolbox, cxpb=0.5, mutpb=0.1)
    for ind, fit in zip(offspring, map(toolbox.evaluate, offspring)):
        ind.fitness.values = fit
    pop = toolbox.select(offspring, k=len(pop))

best = tools.selBest(pop, k=1)[0]
print("Best individual:", best)
print("Best fitness:", best.fitness.values[0])