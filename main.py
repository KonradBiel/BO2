from Class_library import Platform, Film_base, PlatformBase
import numpy as np
from algorithm import cost_function, Algorithm

#films_A = Film_base('Baza_filmow_v2.csv')
#
#films_A.base = films_A.base[:150]
#
#A = Platform("Amazon Prime Video", films_A, 32, 1)
#preference_vector = np.zeros(21)
#preference_vector[0] = 1
#print(A.calculate_score(preference_vector))
#
#preference_vector2 = np.zeros(21)
#preference_vector2[1] = 1
#print(A.calculate_score(preference_vector2))



films_A = Film_base('Baza_filmow_v2.csv')

platform_base = PlatformBase('Baza_platform.csv', films_A)

preference_vector2 = np.zeros(21)
preference_vector2[1] = 1

alg = Algorithm(platform_base, preference_vector2)

alg.evolutionary_algorithm()

print(alg.platform_names(alg.individual_with_lowest_cost), alg.cost)