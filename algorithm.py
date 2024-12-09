import random

NUM_Plamforms = 8 # liczba platform
MUTATION_RATE = 0.1 # szansa na mutacje w zakresie od 0-1
GENERATIONS = 50 # Liczba generacji
population_size = 1

def cost_function(platforms, preference_vector):
    cost_fun_val = 0
    for platform in platforms:
        cost_fun_val += platform.calculate_score(preference_vector)
    return cost_fun_val

class Algorithm:
    def __init__(self, platforms, preference_vector):
        self.platforms = platforms
        self.platforms_len = len(platforms)
        self.population = [0] * NUM_Plamforms
        self.preference_vector = preference_vector

    def generate_initial_population(self, population_size = population_size):
        indices = random.sample(range(8), population_size)
        for idx in indices:
            self.population[idx] = 1
        

    def get_list_of_platforms_from_a_binary(self, number = population_size):
        platforms = []
        for i in range(self.platforms_len):
            if number%2 == 1:
                platforms.append(self.platforms[i])
            number = number//2
        return platforms
    
    def crossover(self, parent1, parent2):
        crossover_point = random.randint(1, NUM_Plamforms - 1)
        return parent1[:crossover_point] + parent2[crossover_point:]
    
    def mutate(individual):
        muted_individual = []
        for i in individual:
            if random.random() < MUTATION_RATE:
                muted_individual.append(1 - i)
            else:
                muted_individual.append(i)
        return muted_individual
    
    def evolotionary_algoritm(self, preference_vector):
        self.generate_initial_population(population_size) # stworzenie pierwszej generacji
        population = self.population
        return population
    
    def print_platform_names(self, platform_base):
        platform_names = []

        for i in range(len(self.population)):
            if self.population[i] == 1:
                platform_names.append(platform_base[i].title)

        print(platform_names)
        



class Solution():
    def __init__(self, platforms, preference_vector):
        self.platforms = platforms
        self.score = cost_function(platforms, preference_vector)
        self.cost = sum([x.price for x in platforms])

    def __str__(self):
        return f"Platformy: {[x.title for x in self.platforms]}; Wynik: {self.score}; Koszt: {self.cost};"