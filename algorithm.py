import random
import numpy as np

def cost_function(platforms, preference_vector):
    cost_fun_val = 0;
    for platform in platforms:
        cost_fun_val += platform.calculate_score(preference_vector)
    return cost_fun_val

class Algorithm:
    def __init__(self, platforms, preference_vector, algorithm_options, platform_base, budget):
        self.platforms = platforms
        self.platforms_len = len(platforms)
        self.preference_vector = preference_vector
        self.algorithm_options = algorithm_options
        self.platform_base = platform_base
        self.budget = budget

    def __generate_initial_population(self):
        population = []
        counter = 0;
        while counter < self.algorithm_options["population_size"]:
            random_int = random.randint(0, 2**self.platforms_len-1)
            individual = Solution(self.__get_list_of_platforms_from_a_number(random_int), self.preference_vector, self.platform_base)
            if individual.cost > self.budget:
                continue
            else:
                population.append(Solution(self.__get_list_of_platforms_from_a_number(random_int), self.preference_vector, self.platform_base))
                counter += 1
        return population

    def __get_list_of_platforms_from_a_number(self, number):
        platforms = []
        for i in range(self.platforms_len):
            if number%2 == 1:
                platforms.append(self.platforms[i])
            number = number//2
        return platforms
    
    def __get_list_of_platforms_from_a_binary_list(self, list):
        platforms = []
        for i in range(len(list)):
            if list[i] == 1:
                platforms.append(self.platform_base[i])
        return platforms
    
    def crossover(self, parent1, parent2):
        crossover_point = random.randint(1, len(parent1.binary) - 1)
        new_binary = parent1.binary[:crossover_point] + parent2.binary[crossover_point:]
        return Solution(self.__get_list_of_platforms_from_a_binary_list(new_binary), self.preference_vector, self.platform_base)

    def mutate(self, individual):
        new_binary = [1 - gene if random.random() < self.algorithm_options["mutation_rate"] else gene for gene in individual.binary]
        if new_binary != individual.binary:
            return Solution(self.__get_list_of_platforms_from_a_binary_list(new_binary), self.preference_vector, self.platform_base)
        else:
            return individual

    def evolutionary_algorithm(self):
        population = self.__generate_initial_population()
        population = sorted(population, key=lambda x: x.score, reverse=True)
        elites = int(np.floor(len(population)*0.1))
        reproducing = int(np.floor(len(population)*0.5))
        best = None;
        for generation in range(self.algorithm_options["max_generations"]):
            sorted_population = sorted(population, key=lambda x: x.score, reverse=True)
            print("Generation ", generation)
            for i in sorted_population:
                print(i)
            new_population = []

            for i in range(elites):
                new_population.append(sorted_population[i])
            counter = 0;
            while counter < self.algorithm_options["population_size"]-elites:
                parent1 = random.choice(sorted_population[:reproducing])
                parent2 = random.choice(population[:reproducing])
                offspring = self.crossover(parent1, parent2)
                offspring = self.mutate(offspring)
                if offspring.cost > self.budget:
                    continue
                else:
                    new_population.append(offspring)
                    counter += 1

            population = sorted(new_population, key=lambda x: x.score, reverse=True)
            best = population[0]
        return best
        


class Solution():
    count = 0
    def __init__(self, platforms, preference_vector, platform_base):
        self.platforms = platforms
        self.platform_base = platform_base
        self.binary = self.__convert_to_binary()
        self.score = cost_function(platforms, preference_vector)
        self.cost = sum([x.price for x in platforms])
        Solution.count += 1

    def __convert_to_binary(self):
        return [1 if x in self.platforms else 0 for x in self.platform_base]

    def __str__(self):
        return f"Platformy: {[x.title for x in self.platforms]}; Wynik: {self.score}; Koszt: {self.cost}; Binarnie: {self.binary}"
    