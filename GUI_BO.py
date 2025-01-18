from Class_library import Platform, Film_base, PlatformBase, User, Film
from algorithm import cost_function, Algorithm
import numpy as np
import tkinter as tk
from tkinter import messagebox
from tkinter import Menu, ttk, StringVar, IntVar, DoubleVar, BooleanVar
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import random

# Domyślne parametry algorytmu
DEFAULT_NUM_PLATFORMS = 8
DEFAULT_MUTATION_RATE = 0.1
DEFAULT_GENERATIONS = 50
DEFAULT_POPULATION_SIZE = 10
DEFAULT_TOURNAMENT = False

user = User()
films_A = Film_base('Baza_filmow_v2.csv')
names_of_films = [name.title for name in films_A.films]
platform_base = PlatformBase('Baza_platform.csv', films_A)

class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Ustawienia okna głównego
        self.title("BO_2")
        self.geometry('1024x640')
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        # Tworzenie menu
        menu = Menu(self)
        item = Menu(menu, tearoff=0)
        item.add_command(label='Panel wyboru', command=lambda: self.show_frame("Choosing_page"))
        item.add_command(label='Funkcja celu', command=lambda: self.show_frame("AlgorithmPage"))
        menu.add_cascade(label='File', menu=item)
        self.config(menu=menu)

        # Kontener dla stron
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Słownik do przechowywania stron
        self.frames = {}

        # Dodanie stron do aplikacji
        for F in (Choosing_page, AlgorithmPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Wyświetlenie strony startowej
        self.show_frame("Choosing_page")

    def on_close(self):
        """Obsługuje zamknięcie okna aplikacji."""
        print("Aplikacja została zamknięta")
        self.quit()
        self.destroy()

    def show_frame(self, page_name):
        """Wyświetla stronę o podanej nazwie."""
        frame = self.frames[page_name]
        frame.tkraise()

class Choosing_page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.user = user

        # Ustawienia siatki
        for i in range(10):
            self.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.grid_columnconfigure(j, weight=1)

        # Etykieta
        label = ttk.Label(self, text="Wybór preferencji i opcji algorytmu", font=("Calibra", 24))
        label.grid(row=0, column=1, columnspan=2, padx=10, pady=10)

        # Pole do wpisania nazwy filmu
        self.movie_name_var = StringVar()
        self.selected_movie_var = StringVar()

        movie_label = ttk.Label(self, text="Wpisz nazwę filmu:")
        movie_label.grid(row=1, column=0, padx=10, pady=5)

        self.movie_entry = ttk.Entry(self, textvariable=self.movie_name_var, width=50)
        self.movie_entry.grid(row=1, column=1, padx=10, pady=5)
        self.movie_entry.bind("<KeyRelease>", self.update_autofill)

        # Dropdown for autocompletion
        self.movie_options = names_of_films
        self.filtered_options = tk.StringVar(value=self.movie_options)
        self.movie_listbox = tk.Listbox(self, listvariable=self.filtered_options, height=10, width=50)
        self.movie_listbox.grid(row=2, column=1, padx=10, pady=5)
        self.movie_listbox.bind("<<ListboxSelect>>", self.select_movie_from_list)

        # Listbox to display selected movies
        self.selected_movies_listbox = tk.Listbox(self, height=10, width=30)
        self.selected_movies_listbox.grid(row=1, column=2, rowspan=4, padx=10, pady=5, sticky="n")

        # Button to confirm selection
        confirm_button = ttk.Button(self, text="Select Movie", command=self.display_selected_movie)
        confirm_button.grid(row=3, column=1, padx=10, pady=10)

        # Parametry algorytmu
        self.budget_var = IntVar(value=DEFAULT_NUM_PLATFORMS)
        self.mutation_rate_var = DoubleVar(value=DEFAULT_MUTATION_RATE)
        self.generations_var = IntVar(value=DEFAULT_GENERATIONS)
        self.population_size_var = IntVar(value=DEFAULT_POPULATION_SIZE)
        self.tournament_var = BooleanVar(value=DEFAULT_TOURNAMENT)

        ttk.Label(self, text="Budżet:").grid(row=5, column=0, padx=10, pady=5, sticky="w")
        ttk.Entry(self, textvariable=self.budget_var).grid(row=5, column=1, padx=10, pady=5)

        ttk.Label(self, text="Współczynnik mutacji:").grid(row=6, column=0, padx=10, pady=5, sticky="w")
        ttk.Entry(self, textvariable=self.mutation_rate_var).grid(row=6, column=1, padx=10, pady=5)

        ttk.Label(self, text="Liczba generacji:").grid(row=7, column=0, padx=10, pady=5, sticky="w")
        ttk.Entry(self, textvariable=self.generations_var).grid(row=7, column=1, padx=10, pady=5)

        ttk.Label(self, text="Rozmiar populacji:").grid(row=8, column=0, padx=10, pady=5, sticky="w")
        ttk.Entry(self, textvariable=self.population_size_var).grid(row=8, column=1, padx=10, pady=5)

        ttk.Label(self, text="Turniej selekcyjny:").grid(row=9, column=0, padx=10, pady=5, sticky="w")
        ttk.Checkbutton(self, variable=self.tournament_var).grid(row=9, column=1, padx=10, pady=5, sticky="w")

        # Button do przejścia na AlgorithmPage
        button1 = ttk.Button(self, text="Uruchom algorytm", command=lambda: self.run_algorithm(controller))
        button1.grid(row=10, column=1, padx=10, pady=10)

    def update_autofill(self, event):
        typed_text = self.movie_name_var.get().lower()
        filtered = [movie for movie in self.movie_options if typed_text in movie.lower()]
        self.filtered_options.set(filtered)

    def select_movie_from_list(self, event):
        selected_index = self.movie_listbox.curselection()
        if selected_index:
            selected_movie = self.movie_listbox.get(selected_index)
            self.movie_name_var.set(selected_movie)

    def display_selected_movie(self):
        selected_movie = self.movie_name_var.get()
        film_object = films_A.get_film_by_title(selected_movie)

        if film_object:
            if selected_movie not in self.selected_movies_listbox.get(0, tk.END):
                user.set_users_films(film_object)
                self.selected_movies_listbox.insert(tk.END, selected_movie)
            else:
                messagebox.showinfo("Info", "Movie is already selected.")
        else:
            messagebox.showerror("Error", "Movie not found!")

    def run_algorithm(self, controller):
        user.set_preferences()
        preference_vector = user.get_preferences()  # Wektor preferencji
        budget_var = self.budget_var.get()
        mutation_rate = self.mutation_rate_var.get()
        generations = self.generations_var.get()
        tournament_var = self.tournament_var.get()
        population_size_var = self.population_size_var.get()
        # Inicjalizacja algorytmu
        alg = Algorithm(platform_base, preference_vector, {
            "mutation_rate": mutation_rate,
            "population_size": population_size_var,
            "max_generations": generations,
            "tournament": tournament_var
        }, platform_base, budget_var)
        best_solution, score_arr = alg.evolutionary_algorithm()

        # Przekaż wyniki do AlgorithmPage
        algorithm_page = controller.frames["AlgorithmPage"]
        algorithm_page.update_plot(len(score_arr), score_arr, best_solution)
        controller.show_frame("AlgorithmPage")


class AlgorithmPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Konfiguracja układu
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Wykres
        self.figure, self.ax = plt.subplots(figsize=(6, 4))
        self.ax.set_title("Zmiana funkcji celu w iteracjach")
        self.ax.set_xlabel("Iteracje")
        self.ax.set_ylabel("Wartość funkcji celu")
        self.line, = self.ax.plot([], [], label="Funkcja celu")
        self.ax.legend()

        self.canvas = FigureCanvasTkAgg(self.figure, self)
        canvas_widget = self.canvas.get_tk_widget()
        canvas_widget.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Etykieta dla najlepszego wyniku
        self.best_result_label = ttk.Label(self, text="Najlepszy wynik: ---", font=("Arial", 12))
        self.best_result_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        # Etykieta dla wybranego wektora platform
        self.selected_platforms_label = ttk.Label(self, text="Wybrane platformy: ---", font=("Arial", 12), wraplength=800)
        self.selected_platforms_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        # Powrót do wyboru
        back_button = ttk.Button(self, text="Powrót", command=lambda: controller.show_frame("Choosing_page"))
        back_button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    def update_plot(self, generations, costs, best_solution):
        # Aktualizacja wykresu
        self.line.set_data(range(generations), costs)
        self.ax.set_xlim(0, generations - 1)
        self.ax.set_ylim(min(costs) - 5, max(costs) + 5)
        self.canvas.draw()

        # Wyświetlenie najlepszego wyniku
        self.best_result_label.config(text=f"Najlepszy wynik: {best_solution.score:.4f}")

        # Wyświetlenie wybranych platform
        platform_titles = [platform.title for platform in best_solution.platforms]
        self.selected_platforms_label.config(
            text=f"Wybrane platformy: {', '.join(platform_titles)}"
        )


# Uruchomienie aplikacji
if __name__ == "__main__":
    app = tkinterApp()
    app.mainloop()