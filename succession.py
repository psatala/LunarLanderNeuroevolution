from population import *

def successionGenerational(stablePopulation, tempPopulation):
    return tempPopulation

def successionElite(stablePopulation, tempPopulation):
    stablePopulation.individuals[::-1].sort()
    elite = stablePopulation.individuals[:ELITE_SIZE]
    alive = []
    if len(tempPopulation.individuals) + ELITE_SIZE > POPULATION_SIZE:
        list.sort(tempPopulation.individuals)
        alive = tempPopulation.individuals[:POPULATION_SIZE-ELITE_SIZE]
    else:
        alive = tempPopulation.individuals
    population = Population()
    population.individuals = elite
    population.individuals.extend(alive)
    return population