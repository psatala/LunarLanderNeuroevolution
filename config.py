import constants

# seed
SEED = 123
MAX_ENV_SEED = 10**9

# network
N_HIDDEN = 16

# general
N_RUNS = 1
N_EPOCHS = 400
# problem size is count of all network parameters (2 layers with bias)
# do not change it unless network architecture is changed
PROBLEM_SIZE = (constants.IN_FEATURES * N_HIDDEN + N_HIDDEN + 
    N_HIDDEN * constants.OUT_FEATURES + constants.OUT_FEATURES)

# evolutionary algorithm
POPULATION_SIZE = 300
CROSSOVER_PROBABILITY = 1.0
MUTATION_PROBABILITY = 0.01
ELITE_SIZE = 240

# chosen methods
SELECTION_METHOD = constants.SELECTION_TOURNAMENT
CROSSOVER_METHOD = constants.CROSSOVER_NONE
MUTATION_METHOD = constants.MUTATION_RANDOM
SUCCESSION_METHOD = constants.SUCCESSION_ELITE

