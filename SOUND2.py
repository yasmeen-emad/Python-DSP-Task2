# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 04:01:49 2018

@author: lenovo
"""

import math


import sounddevice as sd 
import numpy as np
import matplotlib.pyplot as plt
o = math.sin(math.radians(90))

duration1=5
duration2=4
fs=44100
f=300
f1=440
f2=4
t = np.arange(0.0, 400, 0.005)      #np.arange(start, stop=None, step=1)
t1 = np.arange(0.0, 200, 0.005)
#multiply fun
y=np.sin( t )
x=np.cos(t)
z=np.exp(3)
g=y*x*z
plt.plot(g)
plt.show()
sd.play( g)

 #sum fun
sine2=np.sin(2*np.pi*t1)
cose2=np.cos(2*np.pi*t1)
expo2=np.exp(-2)
summ=sine2+cose2+expo2
plt.plot(summ)
plt.show()
sd.play( summ)

plt.show()