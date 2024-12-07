from Class_library import Platform, Film_base, PlatformBase
import numpy as np

# [WORK IN PROGRESS]
# def cost_function(platforms, preference_vector, duplicates):
#     cost_fun_val = 0;
#     for platform in platforms:
#         cost_fun_val += platform.calculate_score(preference_vector)
#     for i, platform1 in enumerate(platforms):
#         for platform2 in platforms[i+1:]:
#             duplicates.get_duplicate_score(platform1, platform2, preference_vector)




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

for platform in platform_base:
    print(platform)