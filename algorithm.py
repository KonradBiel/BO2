import random

NUM_Plamforms = 8 # liczba platform
MUTATION_RATE = 0.1 # szansa na mutacje w zakresie od 0-1
GENERATIONS = 50 # Liczba generacji
population_size = 5 # liczba osobników w jednej populacji

def cost_function(platforms, preference_vector):
    cost_fun_val = 0
    for platform in platforms:
        cost_fun_val += platform.calculate_score(preference_vector)
    return cost_fun_val

class Algorithm:
    def __init__(self, platforms, preference_vector):
        self.platforms = platforms
        self.platforms_len = len(platforms)
        self.population = []
        self.preference_vector = preference_vector
        self.individual_with_lowest_cost = []

    def generate_initial_population(self):
        for _ in range(population_size):
            k = random.randint(1, NUM_Plamforms)
            indices = random.sample(range(NUM_Plamforms), k)
            individual = [0] * NUM_Plamforms
            for idx in indices:
                individual[idx] = 1
            self.population.append(individual)
        

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
    
    def print_platform_names(self, platform_base):
        population_names = []

        for individual in self.population:
            platform_names = []
            print(individual)
            for i in range(len(individual)):
                if individual[i] == 1:
                    platform_names.append(platform_base[i].title)
            population_names.append(platform_names)
        print(population_names)

        
        



class Solution():
    def __init__(self, platforms, preference_vector):
        self.platforms = platforms
        self.score = cost_function(platforms, preference_vector)
        self.cost = sum([x.price for x in platforms])

    def __str__(self):
        return f"Platformy: {[x.title for x in self.platforms]}; Wynik: {self.score}; Koszt: {self.cost};"