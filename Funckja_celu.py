import numpy as np
from movie import Film_base
from movie import GENRES_LIST


class Platform:
    def __init__(self, title, film_base, price):
        self.title = title
        self.film_base = film_base  # Lista obiektów Movie
        self.price = price

    def set_price(self, price):
        self.price = price

    def calculate_preference_correspondence(self, preference_vector):
        """
        Oblicza zgodność preferencji użytkownika z filmami na platformie.
        :param preference_vector: Wektor preferencji użytkownika (lista floatów o długości równej liczbie gatunków).
        :return: Lista par (Movie, score), posortowana malejąco według score.
        """
        if len(preference_vector) != len(GENRES_LIST):
            raise ValueError(f"Preference vector has wrong length. Expected length: {len(GENRES_LIST)}, but got: {len(preference_vector)}.")

        results = []
        for movie in self.film_base.base:
            # Iloczyn skalarny wektora preferencji i wektora gatunków filmu
            score = np.dot(preference_vector, movie.genres_vec)
            results.append((movie, score))
        
        # Sortowanie wyników malejąco według zgodności
        results.sort(key=lambda x: x[1], reverse=True)
        return results
    
# Przykładowy wektor preferencji użytkownika
user_preferences = [0.8, 0.6, 0.2, 0.0, 0.1, 0.0, 0.5, 0.8, 0.6, 0.2, 0.0, 0.1, 0.0, 0.5, 0.8, 0.6, 0.2, 0.0, 0.1, 0.0, 0.0, 0.1,]

# Tworzymy instancję klasy Film_base i wczytujemy dane
film_base_instance = Film_base('Baza_filmow_v2.csv')  # Wprowadź poprawną ścieżkę do pliku z filmami
film_base_instance.set_film_base()  # Wywołujemy funkcję do załadowania filmów

# Oblicz zgodność preferencji użytkownika z filmami
platform = Platform("MyPlatform", film_base_instance, 15.99)
recommendations = platform.calculate_preference_correspondence(user_preferences)

# Wyświetl wyniki
for movie, score in recommendations:
    print(f"Title: {movie.title}, Score: {score:.2f}, Rating: {movie.rating}")
