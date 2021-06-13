#!/usr/bin/env python3

from numpy import average
from operations import *
import copy


def main():

    # Use current Unix time as seed
    seed = SEED
    np.random.seed(seed)

    minReward = []
    avgReward = []
    maxReward = []

    for n in range(N_RUNS):
        print('Run '+str(n))
                
        #initialize population
        stablePopulation = Population()

        mins = []
        avgs = []
        maxs = []

        #main loop
        for i in range(N_EPOCHS):
            if i % 100 == 0:
                print("Epoch "+str(i)+"/"+str(N_EPOCHS))
            tempPopulation = copy.deepcopy(stablePopulation)
            tempPopulation = selection(tempPopulation, SELECTION_METHOD)
            tempPopulation = crossover(tempPopulation, CROSSOVER_METHOD)
            tempPopulation = mutation(tempPopulation, MUTATION_METHOD)
            tempPopulation.calculateReward()
            stablePopulation = succession(stablePopulation, tempPopulation, 
                SUCCESSION_METHOD)
            scores = []
            for x in stablePopulation.individuals:
                scores.append(x.reward)
            mins.append(min(scores))
            avgs.append(round(sum(scores)/len(scores)))
            maxs.append(max(scores))

        
        minReward.append(mins)
        avgReward.append(avgs)
        maxReward.append(maxs)

        print(minReward)
        print(avgReward)
        print(maxReward)
    


if __name__ == "__main__":
    main()

