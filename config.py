import constants

# seed
SEED = 123
MAX_ENV_SEED = 10**9

# network
N_HIDDEN = 16

# general
N_RUNS = 1
N_EPOCHS = 400
N_EVALS = 5
# problem size is count of all network parameters (2 layers with bias)
# do not change it unless network architecture is changed
PROBLEM_SIZE = (constants.IN_FEATURES * N_HIDDEN + N_HIDDEN + 
    N_HIDDEN * constants.OUT_FEATURES + constants.OUT_FEATURES)

# evolutionary algorithm
POPULATION_SIZE = 100
CROSSOVER_PROBABILITY = 0.75
MUTATION_PROBABILITY = 0.01
ELITE_SIZE = 20

# chosen methods
SELECTION_METHOD = constants.SELECTION_TOURNAMENT
CROSSOVER_METHOD = constants.CROSSOVER_UNIFORM
MUTATION_METHOD = constants.MUTATION_RANDOM
SUCCESSION_METHOD = constants.SUCCESSION_ELITE

# path to best model
PATH = "best_model.pt"