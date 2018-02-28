# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 01:14:39 2018

@author: lenovo
"""

import sounddevice as sd 
import numpy as np
import matplotlib.pyplot as plt

duration1=5
duration2=4
fs=44100
f=300
f1=440
f2=4
#multiply fun
y=np.sin(2*np.pi*np.arange(fs*duration1)*f/fs)
x=np.cos(2*np.pi*np.arange(fs*duration1)*f1/fs)
z=np.exp(3)
g=y*x*z
plt.plot(g)
plt.show()
sd.play( g)

 #sum fun
sine2=np.sin(2*np.pi*np.arange(fs*duration2)*f/fs)
cose2=np.cos(2*np.pi*np.arange(fs*duration2)*f2/fs)
expo2=np.exp(-2)
summ=sine2+cose2+expo2
plt.plot(summ)
plt.show()
sd.play( summ)