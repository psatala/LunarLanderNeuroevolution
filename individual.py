import numpy as np
from constants import *
from config import *



class Individual:
    def __init__(self):
        self.reward = -1e9
        self.chromosome = np.zeros(PROBLEM_SIZE)
        for i in range (PROBLEM_SIZE):
            self.reinitialize_element(i)

    def __lt__(self, other): 
        return self.reward < other.reward


    def calculateReward(self, seed):
        self.reward = eval(self.chromosome, seed)
        return self.reward

    def reinitialize_element(self, index):
        # first linear layer
        if index < IN_FEATURES * N_HIDDEN + N_HIDDEN:    
            self.chromosome[index] = np.random.uniform(-1. / IN_FEATURES, 
                1. / IN_FEATURES)
            return
        
        # second linear layer
        self.chromosome[index] = np.random.uniform(-1. / N_HIDDEN, 
            1. / N_HIDDEN)
