from genres import ALL_GENRES
import numpy as np

class Film:
    def __init__(self, title, genres, watch_time, rating, film_id):
        self.title = title
        self.rating = int(rating)
        self.genres = genres
        self.watch_time = watch_time
        self.film_id = film_id
        self.score_cache = None
        self.preference_reference = None
        self.create_genres_vector(self.genres)

    def create_genres_vector(self, genres):

        genres = [genre for genre in genres if genre != ""]
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


class Film_base:
    def __init__(self, file_name):
        self.films = self.load_films(file_name)  
    
    def load_films(self, file_name):
        films = []
        with open(file_name, 'rt', encoding='utf-8') as file:
            for line in file:
                film_data = line.rstrip().split(';')
                film_id = int(film_data[6]) 
                title = film_data[0]
                rating = film_data[5]
                watch_time = film_data[4]
                genres = film_data[1:4]

                films.append(Film(title, genres, watch_time, rating, film_id))
        return films
    
    def get_film_by_title(self, title):
        for film in self.films:
            if film.title == title:
                return film
        return None

class Platform:
    def __init__(self, title, film_base, price, index, movie_indices):
        self.title = title
        self.films = [film for film in film_base if film.film_id in movie_indices]
        self.price = price
        self.index = index
        self.score_cache = None;
        self.preference_reference = None;
    
    def calculate_score(self, preference_vector):
        if self.score_cache is None or preference_vector is not self.preference_reference:
            self.preference_reference = preference_vector;
            score = 0;
            for film in self.films:
                score += film.get_movie_score(preference_vector)
            self.score_cache = score
        return self.score_cache
    
    def __str__(self):
        return f"Platforma: {self.title}, Cena: {self.price}"
    
class PlatformBase:
    def __init__(self, file_name, film_base):
        self.file_name = file_name
        self.platforms = []
        self.set_platforms(film_base)

    def set_platforms(self, film_base):
        with open(self.file_name, 'rt', encoding='utf-8') as file:
            for line in file:
                platform_data = line.rstrip().split(';')
                title = platform_data[0]
                movie_indices_range = platform_data[1].strip('[]').split(':')
                movie_indices = list(range(int(movie_indices_range[0]), int(movie_indices_range[1]) + 1))
                price = int(platform_data[2])
                index = int(platform_data[3])

                
                platform = Platform(title, film_base.films, price, index, movie_indices)
                self.platforms.append(platform)
    
    def __iter__(self):
        return iter(self.platforms)
    
    def __str__(self):
        return f"PlatformBase: {[x.title for x in self.platforms]}"
    
    def __getitem__(self, index):
        return self.platforms[index]
    
    def __len__(self):
        return len(self.platforms)

class User:
    def __init__(self):
        self.budget = 100
        self.num_of_platf = 0
        self.Users_films = []
        self.preference_vec = []
        self.pref_time = 0

        
    def set_budget(self,budget):
        self.budget = budget
        
        
    # def retain_top_3(self, avg_movie_genres):
    #     top_3 = sorted(avg_movie_genres, reverse=True)[:3]
    #     result = [x if x in top_3 and top_3.remove(x) is None else 0 for x in avg_movie_genres]
    #     return result

    def set_users_films(self, film):
        self.Users_films.append(film)

    def set_preferences(self):
        if not self.Users_films:
            raise Exception("User has no films to calculate preferences.")
        avg_film = sum(film.genres_vec for film in self.Users_films)
        norma = np.linalg.norm(avg_film)
        normalized_film = avg_film/norma
        
        self.preference_vec = normalized_film

                
    def get_budget(self):
        return self.budget
    
    def get_preferences(self):
        return self.preference_vec          
        



# klient = User()
# films_A = Film_base('Baza_filmow_v2.csv')
# for film, i in zip(films_A.films, range(10)):
#     klient.set_users_films(film)
#     print(film.genres_vec)


    
# klient.set_preferences()
# print(klient.get_preferences())  