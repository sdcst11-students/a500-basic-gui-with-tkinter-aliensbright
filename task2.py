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
window.configure(bg='white')

dogphoto = PhotoImage(file="dog.png")
label1 = tk.Label(window, image=dogphoto, width=100, bg="white")
label2 = tk.Label(window, text='Client Database',bg='white')

label3 = tk.Label(window, text='         Name           ', bg="white")
label4 = tk.Label(window, text='         Type           ', bg="white")
label5 = tk.Label(window, text='         Breed          ', bg="white")
label6 = tk.Label(window, text='         Owner          ', bg="white")
label7 = tk.Label(window, text='       Birthdate        ', bg="white")

button1 = tk.Button(window, text='Search by Name')
button2 = tk.Button(window, text='< Previous')
button3 = tk.Button(window, text='Save Entry', bg="#cccccc")
button4 = tk.Button(window, text='Next >')

entry1 = tk.Entry(window, border=2)

entry2 = tk.Entry(window, borderwidth=2, width=17)
entry3 = tk.Entry(window, borderwidth=2, width=17)
entry4 = tk.Entry(window, borderwidth=2, width=17)
entry5 = tk.Entry(window, borderwidth=2, width=17)
entry6 = tk.Entry(window, borderwidth=2, width=17)

label1.grid(row=1,column=1, rowspan=4)

label3.grid(row=5,column=1)
label4.grid(row=5,column=2)
label5.grid(row=5,column=3)
label6.grid(row=5,column=4)
label7.grid(row=5,column=5)

entry2.grid(row=6,column=1)
entry3.grid(row=6,column=2)
entry4.grid(row=6,column=3)
entry5.grid(row=6,column=4)
entry6.grid(row=6,column=5)

button2.grid(row=7,column=1,rowspan=2)
button3.grid(row=7,column=3,rowspan=2)
button4.grid(row=7,column=5,rowspan=2)

button1.grid(row=1,column=4)
entry1.grid(row=1,column=5)
label2.grid(row=2,column=3, rowspan=2)

window.mainloop()