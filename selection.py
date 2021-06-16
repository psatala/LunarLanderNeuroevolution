from population import *



def selectionRoulette(stablePopulation):
    selectedPopulation = Population(populationSize=0)

    #calculate total reward
    rewardVals = []
    for i in range(len(stablePopulation.individuals)):
        rewardVals.append(stablePopulation.individuals[i].reward)
    
    # maxReward = max(rewardVals)
    minReward = min(rewardVals)
    rewardVals -= minReward # get rid of negative rewards
    sumReward = sum(rewardVals)

    #calculate probabilities
    probabilities = np.zeros(len(stablePopulation.individuals))
    for i in range(len(stablePopulation.individuals)):
        probabilities[i] = rewardVals[i] / sumReward

    #select
    chosenOnes = np.random.choice(a=stablePopulation.individuals, 
        size=len(stablePopulation.individuals), replace=True, 
        p=probabilities).tolist()
    selectedPopulation.individuals += chosenOnes

    return selectedPopulation



def selectionTournament(stablePopulation):
    selectedPopulation = Population(populationSize=0)

    for i in range(len(stablePopulation.individuals)):
        #play tournament
        candidate0Id = np.random.randint(0, len(stablePopulation.individuals))
        candidate1Id = np.random.randint(0, len(stablePopulation.individuals))
        if(stablePopulation.individuals[candidate0Id].reward >= 
            stablePopulation.individuals[candidate1Id].reward):
            selectedPopulation.individuals.append(
                stablePopulation.individuals[candidate0Id])
        else:
            selectedPopulation.individuals.append(
                stablePopulation.individuals[candidate1Id])

    
    return selectedPopulation
