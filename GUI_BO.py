import genres as gen
import platforms
import movie
#import client
import numpy as np
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import Menu

#client1 = client.Client()


# ###################### Geometry ###########################

# root = Tk()
# root.title("BO_2")
# root.geometry('1024x640')
# root.columnconfigure(0,weight = 100)
# root.columnconfigure(1, weight= 10)
# root.columnconfigure(2, weight= 10)
# root.rowconfigure(0,weight=1)
# root.rowconfigure(1,weight=1)
# root.rowconfigure(2,weight=1)


# ########################## Up Bar ans his functions #########################




# Tutaj ustawiamy pasek górny i jego przyciski
# menu = Menu(root)
# item = Menu(menu)
# item.add_command(label='Funkcja celu',command= clicked_to_set_budget)
# item.add_command(label='Panel główny')
# menu.add_cascade(label='File', menu=item)
# root.config(menu=menu)

# root.frame()

# adding a label to the root window
# lbl = Label(root, text = "Are you a Geek?")
# lbl.grid()

# adding Entry Field
# budget_box = Entry(root, width=10)
# budget_box .grid(column =1, row =0)



# ######################### Function to buttom #######################
# def clicked_to_set_budget():
#     try:
#         int(budget_box.get())
#         budget = int(budget_box.get())
#         client1.set_budget(budget)
        
#     except ValueError:    
#         messagebox.showerror("Uwaga","Nie dałeś intigera Byku")
       
    
    
# def clicked():
#     pass
    

# def clicked():

#     res = "You wrote" + txt.get()
#     lbl.configure(text = res)        

# #################### Buttoms ##########################
# btn = Button(root, text = "Budget" ,fg = "red", command=clicked_to_set_budget)
# btn.grid(column=2, row=0)

# btn = Button(root, text = "Click me" , fg = "green", command=clicked)
# btn.grid(column=2, row=1)

# btn = Button(root, text = "Click me" ,fg = "blue", command=clicked)
# btn.grid(column=2, row=2)

# ######################################################
# Execute Tkinter



# Klasa głównego okna aplikacji
# Klasa głównego okna aplikacji
class tkinterApp(tk.Tk):

    def __init__(self, *args, **kwargs): 
        tk.Tk.__init__(self, *args, **kwargs)

        # Ustawienia okna głównego
        self.title("BO_2")
        self.geometry('1024x640')

        # Tworzenie menu
        menu = Menu(self)
        item = Menu(menu, tearoff=0)
        item.add_command(label='Panel wyboru', command=lambda: self.show_frame("Choosing_page"))
        item.add_command(label='Funkcja celu', command=lambda: self.show_frame("Page1"))
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
        for F in (Choosing_page, Page1):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Wyświetlenie strony startowej
        self.show_frame("Choosing_page")

    def show_frame(self, page_name):
        """Wyświetla stronę o podanej nazwie."""
        frame = self.frames[page_name]
        frame.tkraise()

# Strona startowa (Choosing_page)
class Choosing_page(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        
        # Etykieta
        label = ttk.Label(self, text="Preferencje", font=("Helvetica", 16))
        label.grid(row=0, column=0, padx=10, pady=10)

        # Przycisk do przejścia na Page1
        button1 = ttk.Button(self, text="Page 1",
                             command=lambda: controller.show_frame("Page1"))
        button1.grid(row=1, column=0, padx=10, pady=10)

# Strona Page1
class Page1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Etykieta
        label = ttk.Label(self, text="Page 1", font=("Helvetica", 16))
        label.grid(row=0, column=4, padx=10, pady=10)

        # Przycisk powrotu do strony startowej
        button1 = ttk.Button(self, text="StartPage",
                             command=lambda: controller.show_frame("Choosing_page"))
        button1.grid(row=1, column=1, padx=10, pady=10)

# Uruchomienie aplikacji
if __name__ == "__main__":
    app = tkinterApp()
    app.mainloop()
