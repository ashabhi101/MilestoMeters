# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 21:25:40 2018

@author: HP
"""

from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(miles.get())
        meters.set(1.60934*value*1000)
    except ValueError:
        pass

root = Tk()
root.title("Miles to Meters")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0,row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

miles = StringVar()
meters = StringVar()

miles_entry = ttk.Entry(mainframe, width=7, textvariable=miles)
miles_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=meters).grid(column=2,row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command= calculate).grid(column=3, row=3, sticky=W)


ttk.Label(mainframe, text="miles").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row = 2, sticky=E)
ttk.Label(mainframe, text = "meters").grid(column=3, row =2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
miles_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()