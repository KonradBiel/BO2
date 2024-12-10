import genres as gen
import platforms
import movie
import client
import numpy as np
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

client1 = client.Client()

# create root window
root = Tk()

# root window title and dimension
root.title("BO_2")

####################### Geometry ###########################
root.geometry('1024x640')
root.columnconfigure(0,weight = 100)
root.columnconfigure(1, weight= 10)
root.columnconfigure(2, weight= 10)
root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=1)
root.rowconfigure(2,weight=1)

# adding menu bar in root window
# new item in menu bar labelled as 'New'
# adding more items in the menu bar 
menu = Menu(root)
item = Menu(menu)
item.add_command(label='Funkcja celu',command=)
item.add_command(label='Panel główny')
menu.add_cascade(label='File', menu=item)
root.config(menu=menu)

root.frame()

# adding a label to the root window
lbl = Label(root, text = "Are you a Geek?")
lbl.grid()

# adding Entry Field
budget_box = Entry(root, width=10)
budget_box .grid(column =1, row =0)



########################## Function to buttom #######################
def clicked_to_set_budget():
    try:
        int(budget_box.get())
        budget = int(budget_box.get())
        client1.set_budget(budget)
        
    except ValueError:    
        messagebox.showerror("Uwaga","Nie dałeś intigera Byku")
       
    
    
def clicked():

    

def clicked():

    res = "You wrote" + txt.get()
    lbl.configure(text = res)        

##################### Buttoms ##########################
btn = Button(root, text = "Budget" ,fg = "red", command=clicked_to_set_budget)
btn.grid(column=2, row=0)

btn = Button(root, text = "Click me" , fg = "green", command=clicked)
btn.grid(column=2, row=1)

btn = Button(root, text = "Click me" ,fg = "blue", command=clicked)
btn.grid(column=2, row=2)

#######################################################
# Execute Tkinter
root.mainloop()












class tkinterApp(Tk):

    def __init__(self, *args, **kwargs): 
        Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = Frame(self)  
        container.pack(side = "top", fill = "both", expand = True) 
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}  

        for F in (StartPage, Page1):
  
            frame = F(container, self)
            self.frames[F] = frame 
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
# first window frame startpage
  
class StartPage(Frame):
    def __init__(self, parent, controller): 
        Frame.__init__(self, parent)
         
        # label of frame Layout 2
        label = ttk.Label(self, text ="Startpage")
         
        # putting the grid in its place by using
        # grid
        label.grid(row = 0, column = 4, padx = 10, pady = 10) 
  
        button1 = ttk.Button(self, text ="Page 1",
        command = lambda : controller.show_frame(Page1))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
     
  
          
  
  
# second window frame page1 
class Page1(Frame):
     
    def __init__(self, parent, controller):
         
        Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Page 1")
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="StartPage",command = lambda : controller.show_frame(StartPage))
     
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
  
  

  
# Driver Code
app = tkinterApp()
app.mainloop()