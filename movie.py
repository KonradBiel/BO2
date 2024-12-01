from genres import GENRES_LIST
import numpy as np


# data = []
# naglowki = ["tytuł", "Gatunek_1","Gatunek_2","Gatunek_3","czas","ocena"]
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
        self.create_genres_vector(self.genres)

    def create_genres_vector(self, genres):
        if len(genres) > 3:
            genres = genres[:3]
        self.genres_vec = np.zeros(len(GENRES_LIST))
        match len(genres):
            case 0:
                raise Exception("Movie doesn't have any genres")
            case 1:
                ind = GENRES_LIST.index(genres[0])
                self.genres_vec[ind] = 1
            case 2:
                ind1 = GENRES_LIST.index(genres[0])
                ind2 = GENRES_LIST.index(genres[1])
                self.genres_vec[ind1] = 2/np.sqrt(5)
                self.genres_vec[ind2] = 1/np.sqrt(5)
            case 3:
                ind1 = GENRES_LIST.index(genres[0])
                ind2 = GENRES_LIST.index(genres[1])
                ind3 = GENRES_LIST.index(genres[2])
                self.genres_vec[ind1] = 4/np.sqrt(21)
                self.genres_vec[ind2] = 2/np.sqrt(21)
                self.genres_vec[ind3] = 1/np.sqrt(21)

class Film_base:
    def __init__(self, file_name):
        self.file_name = file_name
        self.base =[]

    def set_film_base(self):
        with open(f'{self.file_name}', 'rt') as file:
            for line in file:
                film = line.rstrip().split(';')
                self.base.append(Movie[film[0],film[5],film[1:3],film[4]])
                
    set_film_base()



class Platform:
    def __init__(self, title, film_base, price):
        self.title = title
        self.film_base  = film_base 
        self.price = price
    
    def set_price(self,price):
        self.price = price




def calculate_preference_correspondence(self, preference_vector):
    pass


A = Film_base('Baza_filmow_v2.csv')
print(A)