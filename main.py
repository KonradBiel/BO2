from platforms import Platform, Film_base
import numpy as np

# [WORK IN PROGRESS]
# def cost_function(platforms, preference_vector, duplicates):
#     cost_fun_val = 0;
#     for platform in platforms:
#         cost_fun_val += platform.calculate_score(preference_vector)
#     for i, platform1 in enumerate(platforms):
#         for platform2 in platforms[i+1:]:
#             duplicates.get_duplicate_score(platform1, platform2, preference_vector)

films_A = Film_base('Baza_filmow_v2.csv')
A = Platform("Max", films_A, 32)
preference_vector = np.zeros(21)
preference_vector[0] = 1
print(A.calculate_score(preference_vector))

preference_vector2 = np.zeros(21)
preference_vector2[1] = 1
print(A.calculate_score(preference_vector2))