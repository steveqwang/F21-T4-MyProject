from population import Population
import timeit


def main():
    pop_size = 100
    target = "To be or not to be."
    mutation_rate = 0.01
    run_time = 20
    average_generation = 0

    start = timeit.default_timer()

    for i in range(run_time):
        pop = Population(target, pop_size, mutation_rate)
        # you don't need to call this function when the ones right bellow are fully implemented

        # pop.print_population_status()

        # Uncomment these lines bellow when you implement all the functions
        while not pop.finished:
            pop.natural_selection()
            pop.generate_new_population()
            pop.evaluate()
            # pop.print_population_status()

        pop.print_population_status()
        print("GA: " + str(int(i+1)) + "/" + str(run_time))
        average_generation += pop.generations

    stop = timeit.default_timer()

    print()
    print("Average of generations (20 executions): ", average_generation/run_time)
    print('Execution Time: ', stop - start)

if __name__ == "__main__":
    main()
