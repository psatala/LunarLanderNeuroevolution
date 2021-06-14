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

    for _ in range(POPULATION_SIZE):
        # since tempPopulation has already gone through the selection process, 
        # we can just uniformly sample an individual
        a = tempPopulation.individuals[
            np.random.randint(len(tempPopulation.individuals))]

        # do the crossover
        if np.random.rand() < CROSSOVER_PROBABILITY:
            b = tempPopulation.individuals[
                np.random.randint(len(tempPopulation.individuals))]

            if crossoverMethod == CROSSOVER_SINGLE_POINT:
                newPopulation.individuals.append(crossoverSinglePoint(a, b))
            elif crossoverMethod == CROSSOVER_UNIFORM:
                newPopulation.individuals.append(crossoverUniform(a, b))
            else: # CROSSOVER_ARITHMETIC
                newPopulation.individuals.append(crossoverArithmetic(a, b))

        # no crossover
        else:
            newPopulation.individuals.append(a)

    return newPopulation




def mutation(tempPopulation, mutationMethod):
    return mutationRandom(tempPopulation)



def succession(stablePopulation, tempPopulation, successionMethod):
    if successionMethod == SUCCESSION_GENERATIONAL:
        return successionGenerational(stablePopulation, tempPopulation)
    else:
        return successionElite(stablePopulation, tempPopulation)