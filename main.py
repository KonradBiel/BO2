from Class_library import Platform, Film_base, PlatformBase
import numpy as np
from algorithm import cost_function, Algorithm, Solution

films_A = Film_base('Baza_filmow_v2.csv')

platform_base = PlatformBase('Baza_platform.csv', films_A)

preference_vector2 = np.zeros(21)
preference_vector2[1] = 1

alg = Algorithm(platform_base, preference_vector2, {"mutation_rate": 0.1, "population_size": 12, "max_generations": 6, "tournament": True}, platform_base, 35)
best, score_arr = alg.evolutionary_algorithm();
print("Best: ", best)
print("arr: ", score_arr)
print(Solution.count)