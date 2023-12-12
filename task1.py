#!python3
'''
Create the user interface described in the image task1.png.
You should use only the .pack() or .grid() methods
(2 points) 
'''
import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("tk")
window.geometry("420x25")
window.resizable(False,False)
entry1 = tk.Entry(window, borderwidth=2)
entry2 = tk.Entry(window, borderwidth=2)
entry3 = tk.Entry(window, borderwidth=2)
button1 = tk.Button(window, text='x')
button2 = tk.Button(window, text='=')

#entry1.pack(side=LEFT)
#button1.pack(side=LEFT)
#entry2.pack(side=LEFT)
#button2.pack(side=LEFT)
#entry3.pack(side=LEFT)

entry1.grid(row=1,column=1)
button1.grid(row=1,column=2)
entry2.grid(row=1,column=3)
button2.grid(row=1,column=4)
entry3.grid(row=1,column=5)

window.mainloop()
