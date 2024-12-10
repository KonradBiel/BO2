from Class_library import Platform, Film_base, PlatformBase
import numpy as np
from algorithm import cost_function, Algorithm, Solution

films_A = Film_base('Baza_filmow_v2.csv')

platform_base = PlatformBase('Baza_platform.csv', films_A)

for platform in platform_base:
    print(platform)

print(platform_base)

preference_vector2 = np.zeros(21)
preference_vector2[1] = 1
print(cost_function([platform_base[0], platform_base[4]], preference_vector2))
print(cost_function([platform_base[0], platform_base[4], platform_base[5]], preference_vector2))

alg = Algorithm(platform_base, preference_vector2, {"mutation_rate": 0.1, "population_size": 12, "max_generations": 16}, platform_base, 35)
print("Best: ", alg.evolutionary_algorithm())
print(Solution.count)




