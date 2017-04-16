#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 10:49:59 2017

@author: jerry
"""
from bokeh.io import output_file, show
from bokeh.plotting import figure

x = [1,2,3,4,5] 
y = [8,6,5,2,3]

plot = figure()

#Lines and Markers 
plot.line(x, y, line_width=3)
plot.circle(x, y, fill_color='white', size=10)

output_file('line.html')
show(plot)