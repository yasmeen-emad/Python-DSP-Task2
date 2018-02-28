# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 20:16:24 2018

@author: medoz
"""

from tkinter import *
from tkinter import filedialog
import csv
import numpy as np
from  matplotlib import pyplot as plt
from matplotlib import style
import random
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure 

root = Tk()
def load_file():
    root.fileName= filedialog.askopenfilename(filetypes=(("samples files","*.csv"),("All files","*.*")))
    x,y = np.loadtxt(root.fileName,unpack=True,delimiter=',')                                     
    root.title(root.fileName) 
    fig = Figure(figsize=(6,6))
    a = fig.add_subplot(111)
    a.plot(x,y)
    a.set_title ("signal", fontsize=16)
    a.set_ylabel("Y", fontsize=14)
    a.set_xlabel("X", fontsize=14)
    canvas = FigureCanvasTkAgg(fig,root)
    canvas.get_tk_widget().place(x=100,y=300)
    canvas.draw()
    #plt.title ('signal')
    #plt.ylabel ('y')
    #plt.xlabel ('x')
    #plt.plot(x,y)
    #plt.show()  
                  
    text1 = open(root.fileName).read()
   # print(text1)
   # T = Text(root, height=15, width=100)
    #T.place(x=250,y=400)                   
    #T.insert(END,text1) 
root.button = Button(root, text="Browse", width=10,fg='blue') 
root.button.place(x=280,y=60)
root.button.config(command=load_file) 
parameter1 = Label(root, text="parameter1",fg='red')
parameter1.place(x=100,y=100)
parameter2 = Label(root, text="parameter2",fg='blue')
parameter2.place(x=100,y=140) 
parameter3 = Label(root, text="parameter3",fg='black')
parameter3.place(x=100,y=180) 
entry1=Entry(root,width=40)
entry1.place(x=250,y=100)
entry2=Entry(root,width=40)
entry2.place(x=250,y=140)
entry3=Entry(root,width=40)
entry3.place(x=250,y=180) 
bu1=Button(root,text="filter",fg='red', width=10)
def buclick():
    print(entry1.get(),entry2.get(),entry3.get())
   # entry1.delete(0,END)
    #entry2.delete(0,END)
    #entry3.delete(0,END)
    x,y = np.loadtxt(root.fileName,unpack=True,delimiter=',') 
    a= entry1.get()
    b=entry2.get()
    c=entry3.get()
    t=[float(a),float(b),float(c)]
    s= np.convolve(t,y)
    fig = Figure(figsize=(6,6))
    a = fig.add_subplot(111)
    a.plot(s,'red')
    a.set_title ("filterd signal", fontsize=16)
    a.set_ylabel("Y", fontsize=14)
    a.set_xlabel("X", fontsize=14)
    canvas = FigureCanvasTkAgg(fig,root)
    canvas.get_tk_widget().place(x=550,y=300)
    canvas.draw()
    #plt.plot(s)
    #plt.show
bu1.config(command=buclick)  
bu1.place(x=400,y=240)                           
root.mainloop()



