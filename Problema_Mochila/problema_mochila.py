from pyeasyga import pyeasyga
import matplotlib.pyplot as plt
import random

# setup data
data = [{'name': 'green', 'value': 4, 'weight': 12},
        {'name': 'gray', 'value': 2, 'weight': 1},
        {'name': 'yellow', 'value': 10, 'weight': 4},
        {'name': 'orange', 'value': 1, 'weight': 1},
        {'name': 'blue', 'value': 2, 'weight': 2}]

tamanho_populacao = 12

ga = pyeasyga.GeneticAlgorithm(data, population_size=tamanho_populacao,
                               generations=500,
                               crossover_probability=0.9,
                               mutation_probability=0.1,
                               elitism = True,
                               maximise_fitness=True
                               )

cont = 0
aptidoes_por_geracao = []
melhor_por_geracao = []

# For the mutate function, supply one individual (i.e. a candidate
# solution representation) as a parameter,
def mutate(individual):
    mutate_index = random.randrange(len(individual))
    
    mut = random.randrange(0,5)
    
    if mut != 0:
        individual[mutate_index] += 1
    elif mut == 0:
        if individual[mutate_index] != 0:
            individual[mutate_index] -= 1



# define a fitness function
def aptidao(individual, data):
    global cont
    cont += 1
    #print("individual", individual)
    values, weights = 0, 0
    for gene, box in zip(individual, data):
        print(gene, box)
        if gene != 0:
            values += box['value']*gene
            weights += box['weight']*gene
    if weights > 15:
        values = 0
    #print(values)
    #print()
    aptidoes_por_geracao.append(values)
    if(cont >= tamanho_populacao):
      print(aptidoes_por_geracao)
      melhor_por_geracao.append( max(aptidoes_por_geracao) )
      aptidoes_por_geracao.clear()
      cont = 0
    return values

ga.mutate_function = mutate
ga.fitness_function = aptidao
ga.run()
print(ga.best_individual())
plt.plot(melhor_por_geracao)
plt.savefig('graph.jpg')