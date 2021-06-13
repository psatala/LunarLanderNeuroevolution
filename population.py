from individual import *



# def printPop(pop):
#     for x in pop.individuals:
#         print(x.chromosome, end=' ')
#         print(x.fitness, end='\t')
#     print()

# def bestFitness(pop):
#     bestFit = 1e9
#     for x in pop.individuals:
#         if x.fitness < bestFit:
#             bestFit = x.fitness
#     print(bestFit)


class Population:
    def __init__(self, populationSize = POPULATION_SIZE):
        self.individuals = [Individual() for _ in range(populationSize)]

    def calculateReward(self):
        seed = 0
        for individual in self.individuals:
            individual.calculateReward(seed=seed)