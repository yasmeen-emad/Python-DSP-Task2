# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 12:23:18 2018

@author: a
"""
import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import matplotlib.pyplot as plt

time_of_view        = 1.; # s.
analog_time         = np.linspace (0, time_of_view, 10e5); # s.

sampling_rate       = 20.; # Hz
sampling_period     = 1. / sampling_rate; # s
sample_number       = time_of_view / sampling_period;
sampling_time       = np.linspace (0, time_of_view, sample_number);

carrier_frequency   = 9.;
amplitude           = 1;
phase               = 0;

quantizing_bits     = 4;
quantizing_levels   = 2 ** quantizing_bits / 2;
quantizing_step     = 1. / quantizing_levels;

def analog_signal (time_point):
    return amplitude * np.cos (2 * np.pi * carrier_frequency * time_point + phase);
sampling_signal     = analog_signal (sampling_time);
quantizing_signal   = np.round (sampling_signal / quantizing_step) * quantizing_step;


fig = plt.figure ()
plt.plot (analog_time,   analog_signal (analog_time) );
plt.show()
#plt.stem (sampling_time, sampling_signal);
plt.stem (sampling_time, quantizing_signal, linefmt='r-', markerfmt='rs', basefmt='r-');
plt.title("Analog to digital signal conversion")
plt.xlabel("Time")
plt.ylabel("Amplitude")

plt.show()

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Sampling of sinusoids'),

    html.Div(children='''
        Task2 : DSP course
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': analog_time, 'y':  analog_signal (analog_time), 'type': 'bar', 'name': 'sampled signal'},
            ],
            'layout': {
                'title': 'Sampling'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)