import tkinter as tk 
import os

def create_folder(name):
 pach_folder= os.pach.mkdir(name)

root = tk.Tk()
root.title ("crear carpeta")
root.geometry("350x350")

name_folder = tk.label(root,text="nombre de la carpeta")

text_name_folder = tk.StringVar()
entry_name_folder = tk.Entry(root,textvariable=text_name_folder)

button = tk.Button(root,text="crear",command=lambda:create_folder(entry_name_folder))

name_folder.grid(column=0,row=0)
entry_name_folder.grid(column=1, row=0)
button .grid(column=0,row=1)


root.mainloop()
