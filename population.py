from individual import Individual
import random


class Population:
    """
        A class that describes a population of virtual individuals
    """

    def __init__(self, target, size, mutation_rate):
        self.population = []
        self.generations = 0
        self.target = target
        self.mutation_rate = mutation_rate
        self.best_ind = None
        self.finished = False
        self.perfect_score = 1.0
        self.max_fitness = 0.0
        self.average_fitness = 0.0
        self.mating_pool = []

        for i in range(size):
            ind = Individual(len(target))
            ind.calc_fitness(target)

            if ind.fitness > self.max_fitness:
                self.max_fitness = ind.fitness

            self.average_fitness += ind.fitness
            self.population.append(ind)

        self.average_fitness /= size

    def print_population_status(self):
        print("\nPopulation " + str(self.generations))
        print("Average fitness: " + str(self.average_fitness))
        print("Best individual: " + str(self.best_ind))

    # Generate a mating pool according to the probability of each individual
    def natural_selection(self):
        # Implementation suggestion based on Lab 3:
        # Based on fitness, each member will get added to the mating pool a certain number of times
        # a higher fitness = more entries to mating pool = more likely to be picked as a parent
        # a lower fitness = fewer entries to mating pool = less likely to be picked as a parent

        ind_prob = []
        for i in range(len(self.population)):
            ind_prob.append(self.population[i].fitness)
        # refill the mating_pool according to the corresponding probabilities
        self.mating_pool = random.choices(self.population, ind_prob, k=len(self.population))

    # Generate the new population based on the natural selection function
    def generate_new_population(self):
        ## self.population = []
        # self.generations = 0
        for i in range(0, len(self.population), 2):
            child = self.mating_pool[i].crossover(self.mating_pool[i+1])
            child.mutate(self.mutation_rate)
            self.population[i] = child
            self.population[i+1] = self.mating_pool[i+1]

        self.average_fitness = 0
        for i in range(len(self.population)):
            curr = self.population[i]
            curr.calc_fitness(self.target)
            curr_fitness = float(self.population[i].fitness)
            self.average_fitness += curr_fitness
            if curr_fitness > self.max_fitness:
                self.max_fitness = curr_fitness
                self.best_ind = curr
        self.average_fitness /= len(self.population)
        self.generations += 1

    # Compute/Identify the current "most fit" individual within the population
    def evaluate(self):
        for i in range(len(self.population)):
            curr_fitness = self.population[i].fitness
            if curr_fitness == self.perfect_score:
                self.finished = True