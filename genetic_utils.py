from random import randint, choice


class SelectionType(Enum):
    RW = auto()   # Roulette Wheel
    BestFitness = auto()
    Tournament = auto()


class CrossoverType(Enum):
    OnePoint = auto()
    Uniform = auto()


def roulette_wheel(fitnesses, scale_factor=100):
    """
    returns index of a random selected chromosome from given fitnesses.
        It has a natural bias towards candidate with higher fitness. 
    Args:
        fitnesses: list(float)   # between 0-1
        scale_factor: float
            precision of the fitness value.
    Returns:
        selected_index: int
            index of the selected chromosome
            0 <= selected_index < len(fitnesses)
    Raises:
        ValueError: no chromosome present in the population.
    """
    if len(fitnesses) < 1:
        raise ValueError("Cannot select from an empty set")
    max_sum = sum(fitnesses)
    rand = randint(0, max_sum * scale_factor) / scale_factor
    partial_sum = 0
    for i in range(len(fitnesses)):
        partial_sum += fitnesses[i]
        if partial_sum >= rand:
            return i


def best_fit(fitnesses):
    """
    returns index of the selected candidate based on the fitness values.
    """
    return fitnesses.index(max(fitnesses))


def tournament_selection(fitnesses):
    """
    Return best of the k randomly selected chromosomes
    k is considered to be random in this case.
    """
    k = randint(1, len(fitnesses))
    best = -1
    for i in range(k):
        rand_fit = choice(fitnesses)
        if best == -1 or rand_fit > best:
            best = rand_fit
    return fitnesses.index(best)


class CrossOvers:
    # Performing crossover on integer representation of chromosome.
    # each digit in the given decimal number is a gene.
    def one_point(c1, c2):
        c1, c2 = map(str, (c1, c2))
        if len(c1) != len(c2):
            raise ValueError("both chromosomes should have same length")
        pivot = randint(0, len(c1))
        # pivot == 0 will indicate no crossover
        
        return int(c1[:pivot] + c2[pivot:]), int(c2[:pivot] + c1[pivot:])
    
    def uniform(c1, c2):
        c1, c2 = map(lambda x: map(int, str(x)), (c1, c2))
        res1 = res2 = 0
        for d1, d2 in zip(c1, c2):
            swap = (randint(1, 10) >= 5)
            if swap:
                d2, d1 = d1, d2
            res1 = 10 * (d1 + res1)
            res2 = 10 * (d2 + res2)

