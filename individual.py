import random
import string


class Individual:
    """
        Individual in the population
    """

    def __init__(self, size):
        self.fitness = 0
        self.genes = self.generate_random_genes(size)

    # Fitness function: returns a floating points of "correct" characters
    def calc_fitness(self, target):
        score = 0

        # insert your code to calculate the individual fitness here
        for i in range(len(target)):
            if self.genes[i] == target[i]:
                score += 1

        self.fitness = score/len(target)

    def __repr__(self):
        return ''.join(self.genes) + " -> fitness: " + str(self.fitness)

    @staticmethod
    def generate_random_genes(size):
        genes = []

        for i in range(size):
            genes.append(random.choice(string.printable))

        return genes

    # The crossover function selects pairs of individuals to be mated, generating a third individual (child)
    def crossover(self, partner):
        # Crossover suggestion: child with half genes from one parent and half from the other parent
        ind_len = len(self.genes)
        child = Individual(ind_len)
        flag = random.randint(0, 1)
        half_idx = ind_len // 2
        if flag:
            child.genes = self.genes[0:half_idx]+partner.genes[half_idx:]
        else:
            child.genes = partner.genes[0:half_idx]+self.genes[half_idx:]
        return child

    # Mutation: based on a mutation probability, the function picks a new random character and replace a gene with it
    def mutate(self, mutation_rate):
        # code to mutate the individual here
        ifMutate = random.choices([0, 1], [1-mutation_rate, mutation_rate], k=1)[0]
        char_pool = string.ascii_letters + " " + "."
        if ifMutate:
            idx = int(random.uniform(0, len(self.genes)))
            self.genes[idx] = random.choice(char_pool)



