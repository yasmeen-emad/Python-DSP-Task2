import numpy as np
import matplotlib.pyplot as plt

#play with th sampling rate and maximum frequency
time_of_view        = 1.; # s.
analog_time         = np.linspace (0, time_of_view, 10e5); # s.
#linspace Returns num evenly spaced samples, calculated over the interval [start, stop].
# 10e5 dtype 
sampling_rate       = 20.; # Hz
sampling_period     = 1. / sampling_rate; # s
sample_number       = time_of_view / sampling_period;
sampling_time       = np.linspace (0, time_of_view, sample_number);

max_frequency   = 9.;  # maximum frequency 

## the ratio sampling rate to carrier frequency should be > 2 according to Nyquist Criterion

#the function parameters
amplitude           = 1;
phase               = 0;


#frequency function 
def analog_signal (time_point):
    return amplitude * np.cos (2 * np.pi * max_frequency * time_point + phase);

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



