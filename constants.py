from enum import Enum

# network
IN_FEATURES = 8
OUT_FEATURES = 4

# selection
class SelectionMethod(Enum):
    selection_roulette = "roulette(1)"
    selection_tournament = "tournament(2)"

# crossover
class CrossoverMethod(Enum):
    crossover_single_point = "single point(1)"
    crossover_uniform = "uniform(2)"
    crossover_arithmetic = "arithmetic(3)"
    crossover_none = "none(4)"

# mutation
class MutationMethod(Enum):
    mutation_random = "random(1)"

# succession
class SuccessionMethod(Enum):
    succession_generational = "generational(1)"
    succession_elite = "elite(2)"