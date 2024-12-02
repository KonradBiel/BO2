from movie import Movie

class Film_base:
    def __init__(self, file_name):
        self.file_name = file_name
        self.base =[]
        self.set_film_base()

    def set_film_base(self):
        with open(f'{self.file_name}', 'rt') as file:
            for line in file:
                film = line.rstrip().split(';')
                print(film)
                self.base.append(Movie(film[0],int(film[5]),[x for x in film[1:3] if x != ''],int(film[4])))
                
    def __iter__(self):
        return iter(self.base)



class Platform:
    def __init__(self, title, film_base, price):
        self.title = title
        self.film_base  = film_base 
        self.price = price
        self.score_cache = None;
        self.preference_reference = None;
    
    def set_price(self,price):
        self.price = price

    def calculate_score(self, preference_vector):
        if self.score_cache is None or preference_vector is not self.preference_reference:
            self.preference_reference = preference_vector;
            score = 0;
            for movie in self.film_base:
                score += movie.get_movie_score(preference_vector)
            self.score_cache = score
        return self.score_cache
    
    def find_duplicates(self, other_platform):
        return [x for x in self.film_base if x in other_platform.film_base]