#!python3
'''
Create the user interface described in the image task2.png.
This image was created using the .grid() method, but you can
use .pack() or .place() also
(5 points)
'''
import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("                              T-Town Veterinary Clinic Database")
window.geometry("550x200")
window.resizable(False,False)
window.configure(bg='white')

dogphoto = PhotoImage(file="dog.png")
label1 = tk.Label(window, image=dogphoto, borderwidth=0)
label2 = tk.Label(window, text='Client Database')

label3 = tk.Label(window, text='Name')
label4 = tk.Label(window, text='Type')
label5 = tk.Label(window, text='Breed')
label6 = tk.Label(window, text='Owner')
label7 = tk.Label(window, text='Birthdate')

button1 = tk.Button(window, text='Search by Name')
button2 = tk.Button(window, text='< Previous')
button3 = tk.Button(window, text='Save Entry')
button4 = tk.Button(window, text='Next >')

entry1 = tk

label1.place(x=20,y=0)

window.mainloop()