
from tkinter import *
import tkinter as tk
import webbrowser


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #master frame config
        self.master = master
        self.master.minsize(700,225)
        self.master.maxsize(700,225)
        self.master.title("Web Page Generator")
        self.master.configure(bg="#F0F0F0")
        arg = self.master

        #func to get the entered text
        def body_insert_func():
            body_insert = self.txt_body.get("1.0",'end') #1.0=read from line 1, char 0; end=read until the end
            html_file = open('your_html.html', 'w')

            #set the text into the html
            message = """<html>
            <head></head>
            <body><p>{}</p></body>
            </html>""".format(body_insert)

            #write the message into the html document and close it
            html_file.write(message)
            html_file.close()
            

        #function to open the page
        def open_page():
            webbrowser.open_new_tab('your_html.html')

        #text label
        self.lbl_body = tk.Label(self.master,text='Enter your text:')
        self.lbl_body.grid(row=0,column=0,padx=(30,0),pady=(20,0),sticky=N+W)
        #textbox for entry
        self.txt_body=tk.Text(self.master,height=4)
        self.txt_body.grid(row=1,column=0,columnspan=2,padx=(30,30),pady=(20,0),sticky=E+W)
        #the add button
        self.btn_add = tk.Button(self.master,width=12,height=2,text='Add Body',command=body_insert_func)
        self.btn_add.grid(row=2,column=0,padx=(30,0),pady=(20,10),sticky=N+E+W)
        #the button to create the webpage
        self.btn_create = tk.Button(self.master,width=12,height=2,text='Open Page',command=open_page)
        self.btn_create.grid(row=2,column=1,padx=(30,30),pady=(20,10),sticky=N+E+W)

        

if __name__ == "__main__":
    root = tk.Tk()  #creates the window
    App = ParentWindow(root)  #attached root to tkinter window
    root.mainloop()  #persistent on the screen
