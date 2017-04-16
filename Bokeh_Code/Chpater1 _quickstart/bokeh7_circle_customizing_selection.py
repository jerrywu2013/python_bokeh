#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 10:49:59 2017

@author: jerry
"""
from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.sampledata.iris import flowers

plot = figure(tools='box_select, lasso_select')

plot.circle(flowers['petal_length'],
            flowers['sepal_length'],
            selection_color='red',
            nonselection_fill_alpha=0.2,
            nonselection_fill_color='grey')

output_file('iris_customizing.html')
show(plot)

