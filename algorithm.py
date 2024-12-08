import random

def cost_function(platforms, preference_vector):
    cost_fun_val = 0;
    for platform in platforms:
        cost_fun_val += platform.calculate_score(preference_vector)
    return cost_fun_val

class Algorithm:
    def __init__(self, platforms, preference_vector):
        self.platforms = platforms
        self.platforms_len = len(platforms)
        self.population = []
        self.preference_vector = preference_vector

    def generate_initial_population(self, population_size):
        for _ in range(population_size):
            random_int = random.randint(0, 2**self.platforms_len-1)
            self.population.append(Solution(self.__get_list_of_platforms_from_a_binary(random_int), self.preference_vector))

    def __get_list_of_platforms_from_a_binary(self, number):
        platforms = []
        for i in range(self.platforms_len):
            if number%2 == 1:
                platforms.append(self.platforms[i])
            number = number//2
        return platforms


class Solution():
    def __init__(self, platforms, preference_vector):
        self.platforms = platforms
        self.score = cost_function(platforms, preference_vector)
        self.cost = sum([x.price for x in platforms])

    def __str__(self):
        return f"Platformy: {[x.title for x in self.platforms]}; Wynik: {self.score}; Koszt: {self.cost};"