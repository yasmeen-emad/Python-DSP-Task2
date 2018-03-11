# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 14:09:53 2018

@author: a
"""

import numpy as np
import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly.graph_objs as go
import plotly
plotly.tools.set_credentials_file(username='yasmeen-emad', api_key='iYYilRxytpvIKzpDRDXV')
# Api key:  iYYilRxytpvIKzpDRDXV
#play with th sampling rate and maximum frequency
time_of_view        = 1.; # s.
analog_time         = np.linspace (0, time_of_view, 10e5); # s.

#linspace Returns num evenly spaced samples, calculated over the interval [start, stop].
# 10e5 dtype 
sampling_rate       = 20.;
sampling_time       = np.linspace (0, time_of_view, sampling_rate);

max_frequency   = 9.;  # maximum frequency 

## the ratio sampling rate to max frequency should be > 2 according to Nyquist Criterion

#the function parameters
amplitude           = 1.;
phase               = 0.;


#frequency function 
def analog_signal (time):
    return amplitude * np.cos (2 * np.pi * max_frequency * time + phase);

sampling_signal     = analog_signal (sampling_time);


fig = plt.figure () 
plt.plot (analog_time,   analog_signal (analog_time) );
plt.title(" Signal ")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.show ()

plt.plot (analog_time,   analog_signal (analog_time) );
plt.plot (sampling_time, sampling_signal, 'o')
plt.show() # used to plot the sampling only 


# Create a trace
trace = go.Scatter(
    x = analog_time,
    y = analog_signal (analog_time)
)

data = [trace]

py.iplot(data, filename='basic-line')
