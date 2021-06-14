import torch
from network import Network
from individual import *
import config

class Population:
    def __init__(self, populationSize = POPULATION_SIZE):
        self.individuals = [Individual() for _ in range(populationSize)]

    def calculateReward(self, seeds):
        for individual in self.individuals:
            individual.calculateReward(seeds=seeds)

    def save_best(self):
        net = Network(self.individuals[0].chromosome)
        torch.save(net.state_dict(), PATH)