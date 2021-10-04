#
# Python Ver:   3.9.7
#
# Author:       Beatrice Owens
#
# Purpose:      Phonebook project, using OOP, Tkinter GUI module,
#               Tkinter parent and child relationships
#
# Tested OS:    Written and tested with Windows 10

from tkinter import *
import tkinter as tk
from tkinter import messagebox

#must import the other related modules for access
import phonebook_gui
import phonebook_func


#creating a child class to the tk parent class frame
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define master frame configuration
        self.master = master
        self.master.minsize(500,300) #height, width
        self.master.maxsize(500,300)
        #CenterWindow method centers the app on user's screen
        phonebook_func.center_window(self,500,300)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(bg="#F0F0F0")
        #protocol method is a built-in tkinter method to catch if
        #the user clicks the upper corner "X" on Windows OS
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self)) #ask_quit() is located in phonebook_func.py
        arg = self.master

        #load in the GUI widgets from a separate module
        #keeping code compartmentalized and cluster free
        phonebook_gui.load_gui(self)

        #instatiate the tkinter menu dropdown object
        #this is the menu that will appear at the top of the window
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit",underline=1,accelerator="Ctrl+Q",command=lambda: phonebook_func.ask_quit(self))
        menubar.add_cascade(label="File", underline=0, menu=filemenu)
        helpmenu = Menu(menubar, tearoff=0) # defines the particular drop down colum and tearoff=0 means do not separate from menubar
        helpmenu.add_separator()
        helpmenu.add_command(label="How to use this program")
        helpmenu.add_separator()
        helpmenu.add_command(label="About This Phonebook Demo") # add_command is a child menubar item of the add_cascde parent item
        menubar.add_cascade(label="Help", menu=helpmenu) # add_cascade is a parent menubar item (visible heading)

        self.master.config(menu=menubar, borderwidth='1')
        
        



if __name__ == "__main__":
    root = tk.Tk()  #creates the window
    App = ParentWindow(root)  #attached root to tkinter window
    root.mainloop()  #persistent on the screen
