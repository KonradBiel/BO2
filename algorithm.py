import random

NUM_Plamforms = 8 # liczba platform
MUTATION_RATE = 0.1 # szansa na mutacje w zakresie od 0-1
GENERATIONS = 15 # Liczba generacji
population_size = 5 # liczba osobników w jednej populacji

def cost_function(platforms, preference_vector):
    cost_fun_val = 0
    for platform in platforms:
        cost_fun_val += platform.calculate_score(preference_vector)
    return cost_fun_val

import random

class Algorithm:
    def __init__(self, platforms, preference_vector):
        self.platforms = platforms
        self.platforms_len = len(platforms)
        self.population = []
        self.preference_vector = preference_vector
        self.individual_with_lowest_cost = []
        self.cost = float('inf')

    def __generate_initial_population(self):
        for _ in range(population_size):
            k = random.randint(1, self.platforms_len)
            indices = random.sample(range(self.platforms_len), k)
            individual = [0] * self.platforms_len
            for idx in indices:
                individual[idx] = 1
            self.population.append(individual)

    def get_list_of_platforms_from_an_individual(self, individual):
        return [self.platforms[i] for i in range(len(individual)) if individual[i] == 1]

    def crossover(self, parent1, parent2):
        crossover_point = random.randint(1, len(parent1) - 1)
        return parent1[:crossover_point] + parent2[crossover_point:]

    def mutate(self, individual):
        return [
            1 - gene if random.random() < MUTATION_RATE else gene
            for gene in individual
        ]

    def evolutionary_algorithm(self):
        self.__generate_initial_population()
        for _ in range(GENERATIONS):
            new_population = []
            for _ in range(population_size):
                parent1 = random.choice(self.population)
                parent2 = random.choice(self.population)
                offspring = self.crossover(parent1, parent2)
                offspring = self.mutate(offspring)
                new_population.append(offspring)

            for individual in new_population:
                cost = cost_function(self.get_list_of_platforms_from_an_individual(individual), self.preference_vector)
                if cost < self.cost and cost != 0:
                    self.cost = cost
                    self.individual_with_lowest_cost = individual

            self.population = new_population

    def platform_names(self, individual):
        population_names = []
        for i in range(len(individual)):
            if individual[i] == 1:
                population_names.append(self.platforms[i].title)
        return(population_names)



class Solution():
    def __init__(self, platforms, preference_vector):
        self.platforms = platforms
        self.score = cost_function(platforms, preference_vector)
        self.cost = sum([x.price for x in platforms])

    def __str__(self):
        return f"Platformy: {[x.title for x in self.platforms]}; Wynik: {self.score}; Koszt: {self.cost};"