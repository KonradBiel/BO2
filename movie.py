from genres import ALL_GENRES
import numpy as np


# data = []
# naglowki = ["tytuł", "Gatunek_1","Gatunek_2","Gatunek_3","czas","ocena","indeks"]
# with open('Baza_filmow_v2.csv', 'rt') as file:
#     for line in file:
#         record = line.rstrip().split(';')
#         data.append(record)
# print(data)




class Movie:
    def __init__(self, title, rating, genres, watch_time):
        self.title = title
        self.rating = rating
        self.genres = genres
        self.watch_time = watch_time
        self.score_cache = None
        self.preference_reference = None
        self.create_genres_vector(self.genres)

    def create_genres_vector(self, genres):
        if len(genres) > 3:
            genres = genres[:3]
        self.genres_vec = np.zeros(len(ALL_GENRES))
        match len(genres):
            
            case 0:
                raise Exception("Movie doesn't have any genres")
            case 1:
                ind = ALL_GENRES.index(genres[0])
                self.genres_vec[ind] = 1
            case 2:
                ind1 = ALL_GENRES.index(genres[0])
                ind2 = ALL_GENRES.index(genres[1])
                self.genres_vec[ind1] = 2/np.sqrt(5)
                self.genres_vec[ind2] = 1/np.sqrt(5)
            case 3:
                ind1 = ALL_GENRES.index(genres[0])
                ind2 = ALL_GENRES.index(genres[1])
                ind3 = ALL_GENRES.index(genres[2])
                self.genres_vec[ind1] = 4/np.sqrt(21)
                self.genres_vec[ind2] = 2/np.sqrt(21)
                self.genres_vec[ind3] = 1/np.sqrt(21)

    def __calculate_preference_correspondence(self, preference_vector):
        if len(preference_vector) != len(self.genres_vec):
            raise Exception("length of preference_vector doesn't match the length of genres_vec of the movie")
        return np.dot(self.genres_vec, preference_vector)
    
    def get_movie_score(self, preference_vector):
        if self.score_cache is None or preference_vector is not self.preference_reference:
            self.preference_reference = preference_vector
            if self.rating < 40:
                self.score_cache = 0;
            elif self.rating < 90:
                self.score_cache = self.__calculate_preference_correspondence(preference_vector)*(self.rating-40)/50
            else:
                self.score_cache = self.__calculate_preference_correspondence(preference_vector)
        return self.score_cache





