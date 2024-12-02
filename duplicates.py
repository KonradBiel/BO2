import numpy as np

class Duplicates:
    def __init__(self, platforms):
        self.matrix = np.full((len(platforms), len(platforms)), None, dtype=object)
        self.duplicates_lists_matrix = np.full((len(platforms), len(platforms)), None, dtype=object)
        for i in range(len(platforms)):
            self.matrix[i,i] = 0;
            self.duplicates_lists_matrix[i,i] = [];
        self.platforms = platforms

    def get_duplicates_score(self, platform1, platform2, preference_vector):
        ind1 = self.platforms.index(platform1)
        ind2 = self.platforms.index(platform2)

        if self.matrix[ind1, ind2] is None or self.duplicates_lists_matrix[ind1, ind2] is None:
            self.__calculate_duplicates_score(platform1, platform2, ind1, ind2, preference_vector)
        return self.matrix[ind1, ind2]
    
    def get_duplicates_list(self, platform1, platform2, preference_vector):
        ind1 = self.platforms.index(platform1)
        ind2 = self.platforms.index(platform2)

        if self.matrix[ind1, ind2] is None or self.duplicates_lists_matrix[ind1, ind2] is None:
            self.__calculate_duplicates_score(platform1, platform2, ind1, ind2, preference_vector)
        return self.duplicates_lists_matrix[ind1, ind2]

    def __calculate_duplicates_score(self, platform1, platform2, ind1, ind2, preference_vector):
        self.duplicates_lists_matrix[ind1, ind2] = platform1.get_duplicates(platform2)
        self.duplicates_lists_matrix[ind2, ind1] = self.duplicates_lists_matrix[ind2, ind1]

        self.matrix[ind1, ind2] = self.calculate_score(self.duplicates_lists_matrix[ind1, ind2], preference_vector)
        self.matrix[ind2, ind1] = self.matrix[ind1, ind2]
             
    def calculate_score(self, movies, preference_vector):
        score = 0;
        for movie in movies:
            score += movie.get_movie_score(preference_vector)
        return score
    
    def get_duplicates_score(self, platform1, platfrom2):
        i = self.platforms.index(platform1)
        j = self.platforms.index(platfrom2)
        return self.matrix[i,j]