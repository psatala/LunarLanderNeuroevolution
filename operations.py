from selection import *
from crossover import *
from mutation import *
from succession import *



def selection(stablePopulation, selectionMethod):
    if selectionMethod == SELECTION_ROULETTE:
        return selectionRoulette(stablePopulation)
    else:
        return selectionTournament(stablePopulation)



def crossover(tempPopulation, crossoverMethod):
    if crossoverMethod == CROSSOVER_NONE:
        return tempPopulation
    newPopulation = Population()
    newPopulation.individuals = []
    while len(newPopulation.individuals) < POPULATION_SIZE:
        a = tempPopulation.individuals[
            math.floor(np.random.rand()*len(tempPopulation.individuals))]
        b = tempPopulation.individuals[
            math.floor(np.random.rand()*len(tempPopulation.individuals))]
        newPopulation.individuals.append(a)
        if len(newPopulation.individuals) < POPULATION_SIZE:
            newPopulation.individuals.append(b)
        if (np.random.rand() < CROSSOVER_PROBABILITY and 
            len(newPopulation.individuals) < POPULATION_SIZE):

            if crossoverMethod == CROSSOVER_SINGLE_POINT:
                newPopulation.individuals.append(crossoverSinglePoint(a, b))
            elif crossoverMethod == CROSSOVER_UNIFORM:
                newPopulation.individuals.append(crossoverUniform(a, b))
            elif crossoverMethod == CROSSOVER_ARITHMETIC:
                newPopulation.individuals.append(crossoverArithmetic(a, b))
            else:
                return tempPopulation
    return newPopulation
    



def mutation(tempPopulation, mutationMethod):
    # if mutationMethod == MUTATION_GAUSS:
    #     return mutationGauss(tempPopulation)
    # else:
    return mutationRandom(tempPopulation)



def succession(stablePopulation, tempPopulation, successionMethod):
    if successionMethod == SUCCESSION_GENERATIONAL:
        return successionGenerational(stablePopulation, tempPopulation)
    else:
        return successionElite(stablePopulation, tempPopulation)