from enum import Enum, auto


class SelectionType(Enum):
    RW = auto()   # Roulette Wheel
    SUS = auto()   # Stochastic Universal Sampling
    BestFitness = auto()
    Tournament = auto()


class CrossoverType(Enum):
    OnePoint = auto()
    TwoPoint = auto()
    Uniform = auto()
    Davis = auto()
    And = auto()      # bitwise and
    Xor = auto()      # bitwise xor



def build_initial_population(tagged_sentence):
    """
    Generate Initial population from given word tags for the given sentence.
    For each word, randomly select any tag representing gene forming a chromosome.
    Args:
        sentence: list({word: tags}) => list(dict(str: tags))
            for each word in a sentence, list of probable tags.
    Returns:
        population: list(chromosome). 
            Each chromosome can be represented as integer or a binary sequence of 0 and 1s
    Raises:
        ValueError: Given sentence tags are not in required format.
    """


def fitness(chromosome):
    """
    Returns probability of how fit is a particular allocation(tagging).
    ReturnType: float
    Args:
        chromosome: sequence of bits or an integer.
            represents particular allocation(tags)
    Returns: 
        fitness_value: float value between 0-1
    """


def select(population, fitness, selection_type):
    """
    Select two best parents from the population
    Args:
        population: set(chromosome)
        fitness: list(float)
            ordered list of fitnesses of every chromosome in the population.
        selection_type: one of the enums of SelectionType
            specifies the function to use for selection of new parents.
    Returns:
        parents: list of two chromosomes randomly select with a 
                 bias towards chromosome with higher fitness value.
    Raises:
        ValueError: selection_type is not one of the members of SelectionType
    """


def crossover(parents, crossover_type):
    """
    combining pairs of parents to form new offsprings with a random probability of crossover.
    Args:
        parents: set(chromosome)
            list of selected chromosomes from the population.
        crossover_type: member(CrossoverType)
            which type of crossover to perform on set of parents.
    Returns:
        crossed: set(chromosome)
            new chromosomes based upon the crossover_function or an empty list depending upon the probability of crossover.
    Raises:
        ValueError: if parents has less than 2 chromosomes.
        ValueError: if crossover_type is not the member of CrossoverType
    """


def mutation(children):
    """
    Altering one or more genes from the given chromosome 
        for each chromosome in the set of children
    For each gene, using a random probability to indicate 
        whether or not that gene must be mutated.
    For now, performing only single point mutation.
    Args:
        children: set(children)
            set of chromosomes to be modified
    """


def check_convergence(population, fitness, time_threshold=30, fitness_threshold=0.95):
    """
    convergence takes place when one of the following occurs:
        1. fitness value beyond certain threshold values is reached.
        2. population is very small.
        3. time required has reached beyond a certain threshold.
    Returns:
        converged: bool
            indicates whether the population has converged.
    """

