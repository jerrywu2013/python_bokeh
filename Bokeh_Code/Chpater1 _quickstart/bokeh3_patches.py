#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 10:49:59 2017

@author: jerry
"""
from bokeh.io import output_file, show
from bokeh.plotting import figure

xs = [ [1,1,2,2], [2,2,4], [2,2,3,3] ]
ys = [ [2,5,5,2], [3,5,5], [2,3,4,2] ]

plot = figure()

plot.patches(xs, ys,
             fill_color=['red','blue','green'],
             line_color='white')

output_file('patches.html')
show(plot)