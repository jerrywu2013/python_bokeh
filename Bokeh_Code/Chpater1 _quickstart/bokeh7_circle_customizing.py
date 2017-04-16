#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 10:49:59 2017

@author: jerry
"""
from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.sampledata.iris import flowers as df
from bokeh.plotting import ColumnDataSource

source = ColumnDataSource(df)

plot = figure(tools='box_select, lasso_select')

#Lines and Markers 
plot.circle(x='petal_length',
            y='sepal_length',
            source=source,
            selection_color='red',
            nonselection_fill_alpha=0.2,
            nonselection_fill_color='grey')

output_file('iris_customizing.html')
show(plot)