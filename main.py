#!/usr/bin/env python3

from numpy import average
from operations import *
import copy
from mlflow import log_metric, log_param, start_run, end_run, create_experiment


# path to best model
PATH = "best_model.pt"

def main():

    # Use current Unix time as seed
    seed = SEED
    np.random.seed(seed)

    minReward = []
    avgReward = []
    maxReward = []

    # experiment_isd = create_experiment("ALHE experiment")

    for n in range(N_RUNS):
        print('Run '+str(n))

        start_run()
        log_param("Seed", SEED)
        log_param("N Hidden", N_HIDDEN)
        log_param("N Runs", N_RUNS)
        log_param("N Epochs", N_EPOCHS)
        log_param("N Evals", N_EVALS)
        log_param("Population size", POPULATION_SIZE)
        log_param("Crossover probability", CROSSOVER_PROBABILITY)
        log_param("Mutation probability", MUTATION_PROBABILITY)
        log_param("Elite size", ELITE_SIZE)
        log_param("Selection method", SELECTION_METHOD)
        log_param("Crossover method", CROSSOVER_METHOD)
        log_param("Mutation method", MUTATION_METHOD)
        log_param("Succession method", SUCCESSION_METHOD)
                
        #initialize population
        stablePopulation = Population()

        mins = []
        avgs = []
        maxs = []

        #main loop
        for i in range(N_EPOCHS):
            if i % 100 == 0:
                print("Epoch "+str(i)+"/"+str(N_EPOCHS))

            seeds = []
            for _ in range(N_EVALS):
                seeds.append(np.random.randint(config.MAX_ENV_SEED))
            for individual in range(ELITE_SIZE):
                stablePopulation.individuals[individual].calculateReward(seeds)
            tempPopulation = copy.deepcopy(stablePopulation)
            tempPopulation = selection(tempPopulation, SELECTION_METHOD)
            tempPopulation = crossover(tempPopulation, CROSSOVER_METHOD)
            tempPopulation = mutation(tempPopulation, MUTATION_METHOD)
            tempPopulation.calculateReward(seeds)
            stablePopulation = succession(stablePopulation, tempPopulation, 
                SUCCESSION_METHOD)
            stablePopulation.save_best()

            scores = []
            for x in stablePopulation.individuals:
                scores.append(x.reward)
            mins.append(min(scores))
            avgs.append(round(sum(scores)/len(scores)))
            maxs.append(max(scores))

            print("Epoch: " + str(i))
            print("Min: " + str(mins[-1]))
            print("Avg: " + str(avgs[-1]))
            print("Max: " + str(maxs[-1]))
            print()

            log_metric("Min", mins[-1], step=i)
            log_metric("Avg", avgs[-1], step=i)
            log_metric("Max", maxs[-1], step=i)

        minReward.append(mins)
        avgReward.append(avgs)
        maxReward.append(maxs)

        end_run()

    


if __name__ == "__main__":
    main()

