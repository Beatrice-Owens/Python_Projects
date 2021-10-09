

import shutil
import os
import time
import datetime as dt
from tkinter import *
import tkinter as tk
from tkinter import filedialog



class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #master frame config
        self.master = master
        self.master.minsize(375,345)
        self.master.maxsize(375,345)
        self.master.title("File Transfer Folder Selection")
        self.master.configure(bg="#F0F0F0")
        arg = self.master

        #function to open folder selection window
        def srcBrowseFiles():
            global og_folder_name
            og_folder_name = filedialog.askdirectory(initialdir= "/", title= "Select a Source Folder")
            #change label contents
            lbl_folder_explorer_src.configure(text="Source Folder Selected: " + og_folder_name)
            return og_folder_name

        #function to open folder selection window for destination
        def dstBrowseFiles():
            global dst_folder_name
            dst_folder_name = filedialog.askdirectory(initialdir= "/", title= "Select a Destination Folder")
            #change label contents
            lbl_folder_explorer_dst.configure(text="Destination Folder Selected: " + dst_folder_name)
            return dst_folder_name

        #defining the source & destination
        def copyFiles():
            source = og_folder_name
            destination = dst_folder_name
            files = os.listdir(source)
            #for every file in the selected folder 
            for i in files:
                mod_time = os.path.getmtime(source+"//"+i)
                creation_time = os.path.getctime(source+"//"+i)
                current_time = time.time()
                time_since_mod = current_time - mod_time #determin if 24 hrs have passed by subtracting in epoch time
                if time_since_mod <= 86400:
                    shutil.move(source+"//"+i, destination)
        
        #label to display the chosen source folder
        self.lbl_src = tk.Label(self.master,text='Select Source', width=50, height=2)
        lbl_folder_explorer_src = self.lbl_src
        lbl_folder_explorer_src.grid(row=0,column=1,pady=(20,0),sticky=N+E+W)
        #button that links to folder selection func
        self.btn_src = tk.Button(self.master,width=20,height=2,text='Browse for Source',command = srcBrowseFiles)
        self.btn_src.grid(row=1,column=1,padx=(30,30),pady=(20,10),sticky=N+E+W)
        #label to display the chose destination folder
        self.lbl_src = tk.Label(self.master,text='Select Destination', width=50, height=2)
        lbl_folder_explorer_dst = self.lbl_src
        lbl_folder_explorer_dst.grid(row=2,column=1,pady=(20,0),sticky=N+E+W)
        #button that links to folder selection func
        self.btn_dst = tk.Button(self.master,width=20,height=2,text='Browse for Destination',command = dstBrowseFiles)
        self.btn_dst.grid(row=3,column=1,padx=(30,30),pady=(20,10),sticky=N+E+W)

        self.btn_copy = tk.Button(self.master,width=20,height=2,text='Complete Transfer',command = copyFiles)
        self.btn_copy.grid(row=4,column=1,padx=(30,30),pady=(20,10),sticky=N+E+W)
        
        
        
        



if __name__ == "__main__":
    root = tk.Tk()  #creates the window
    App = ParentWindow(root)  #attached root to tkinter window
    root.mainloop()  #persistent on the screen
