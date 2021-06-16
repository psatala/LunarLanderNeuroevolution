import constants
from datetime import datetime

# seed
SEED = 123
MAX_ENV_SEED = 10**9

# network
N_HIDDEN = 16

# general
N_RUNS = 1
N_EPOCHS = 400
N_EVALS = 5
N_SIM_STEP_LIMIT = 400
# problem size is count of all network parameters (2 layers with bias)
# do not change it unless network architecture is changed
PROBLEM_SIZE = (constants.IN_FEATURES * N_HIDDEN + N_HIDDEN + 
    N_HIDDEN * constants.OUT_FEATURES + constants.OUT_FEATURES)

# evolutionary algorithm
POPULATION_SIZE = 100
CROSSOVER_PROBABILITY = 1
MUTATION_PROBABILITY = 0.01
ELITE_SIZE = 20

# chosen methods
SELECTION_METHOD = constants.SelectionMethod.selection_tournament
CROSSOVER_METHOD = constants.CrossoverMethod.crossover_uniform
MUTATION_METHOD = constants.MutationMethod.mutation_random
SUCCESSION_METHOD = constants.SuccessionMethod.succession_elite

# path to best model
PATH = "models/best_model_"+str(datetime.now()).replace(" ", "").replace(
    ".", "").replace(":", "")+".pt"