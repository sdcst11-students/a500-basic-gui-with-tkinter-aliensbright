#!python3
import tkinter as tk 
from tkinter import *
from tkinter import ttk
'''
Create the user interface described in the image task3.png
using the .place() method
(3 points)
'''

window = tk.Tk()
window.configure(bg='white')
window.title('          Example')
window.geometry('257x140')
window.resizable(False,False)

dogphoto = PhotoImage(file="dog.png")
dog=tk.Label(window, image=dogphoto, bg="white")

pochacco=tk.Label(window,text='Pochacco!                    ', bg="white")
desc=tk.Label(window,text='A cuddly little puppy! This is from the same\ncreators who brought you Keropi and Kero Kero', bg="#aaffff")

dog.place(x=80)
pochacco.place(x=150,y=40)
desc.place(x=0,y=105)


window.mainloop()