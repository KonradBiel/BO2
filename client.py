import genres as gen
import platforms
import movie
import numpy as np


data = []
naglowki = ["tytuł", "Gatunek_1","Gatunek_2","Gatunek_3","czas","ocena"]
with open('Baza_filmow_v2.csv', 'rt') as file:
    for line in file:
        record = line.rstrip().split(';')
        data.append(record)


class Client:
    def __init__(self):
        # Preferencje zapisuje jako pref_vec =[[0 albo 1 dla konkretnych gatunkow], czas trwania lubianego filmu]s  
        self.budget = 100
        self.num_of_platf = 0
        self.preference_vec = [np.zeros(21),self.budget]
        
        
        
    def set_budget(self,budget):
        self.budget = budget
        self.preference_vec[1] = budget
        
    # Tu avg_movie daje jako film "idealny" z wszystkich filmów, które wybrał użytkownik 
    def set_preferences(self, avg_movie):
         for i in range(3):
            for j in range(21):
                if avg_movie.genres[i] == gen.ALL_GENRES[j]:
                    self.preference_vec[0][j] = 1
                
    def get_budget(self):
        return self.budget
        
    # Tu avg_movie daje jako film "idealny" z wszystkich filmów, które wybrał użytkownik 
    def get_preferences(self):
        return self.preference_vec          
        
        
        
        
        
############################# TESTY #####################################        
movie1 = movie.Movie('The Godfather',92,['Crime','Drama',""],175)
movie2 = data[10]
movie2 = movie.Movie(movie2[0],movie2[5],movie2[1:4],movie2[4] )


print('\n')
client1 = Client()
print(client1.preference_vec)
client1.set_preferences(movie1)
client1.set_budget(150)
print(client1.preference_vec)

print('\n')
client2 = Client()
print(client2.preference_vec)
client2.set_preferences(movie2)
client2.set_budget(150)
print(client2.preference_vec)
