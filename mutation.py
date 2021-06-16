from population import *


# mutation sampled from range
def mutationRandom(tempPopulation):
    for i in range(len(tempPopulation.individuals)):
        for j in range(tempPopulation.individuals[i].chromosome.size):
            if np.random.rand() < MUTATION_PROBABILITY:
                tempPopulation.individuals[i].reinitialize_element(j)
    return tempPopulation
