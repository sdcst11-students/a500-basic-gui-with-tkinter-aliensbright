#!python3
import tkinter as tk 
from tkinter import *
from tkinter import ttk
'''
##### Task 3
Create the user interface described in the image task3.png
using the .grid() method
(3 points)
'''
window = tk.Tk()
window.configure(bg='white')
window.title('          Example')

dogphoto = PhotoImage(file="dog.png")
dog=tk.Label(window, image=dogphoto, bg="white")

pochacco=tk.Label(window,text='Pochacco!                    ', bg="white")
desc=tk.Label(window,text='A cuddly little puppy! This is from the same\ncreators who brought you Keropi and Kero Kero',  bg="#aaffff")

desc.grid(row=4,column=1,columnspan=4)
dog.grid(row=1,rowspan=3,column=2)
pochacco.grid(row=2,column=3)

window.mainloop()