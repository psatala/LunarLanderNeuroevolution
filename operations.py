from selection import *
from crossover import *
from mutation import *
from succession import *



def selection(stablePopulation, selectionMethod):
    if selectionMethod == SelectionMethod.selection_roulette:
        return selectionRoulette(stablePopulation)
    else:
        return selectionTournament(stablePopulation)



def crossover(tempPopulation, crossoverMethod):
    if crossoverMethod == CrossoverMethod.crossover_none:
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

            if crossoverMethod == CrossoverMethod.crossover_single_point:
                newPopulation.individuals.append(crossoverSinglePoint(a, b))
            elif crossoverMethod == CrossoverMethod.crossover_uniform:
                newPopulation.individuals.append(crossoverUniform(a, b))
            else: # CrossoverMethod.crossover_arithmetic
                newPopulation.individuals.append(crossoverArithmetic(a, b))

        # no crossover
        else:
            newPopulation.individuals.append(a)

    return newPopulation




def mutation(tempPopulation, mutationMethod):
    return mutationRandom(tempPopulation)



def succession(stablePopulation, tempPopulation, successionMethod):
    if successionMethod == SuccessionMethod.succession_generational:
        return successionGenerational(stablePopulation, tempPopulation)
    else:
        return successionElite(stablePopulation, tempPopulation)