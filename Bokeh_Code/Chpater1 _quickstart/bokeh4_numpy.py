#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 11:16:30 2017

@author: jerry
"""
from bokeh.io import output_file,show
from bokeh.plotting import figure
import numpy as np

x = np.linspace(0, 10, 1000)
y = np.sin(x) + np.random.random(1000) * 0.2
          
plot = figure()

plot.line(x, y)

output_file('numpy.html')
show(plot)


