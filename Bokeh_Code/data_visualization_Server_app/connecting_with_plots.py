#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 09:22:59 2017

@author: jerry
"""

##################################

from bokeh.io import curdoc
from bokeh.layouts import column, widgetbox
from bokeh.models import ColumnDataSource, Slider
from bokeh.plotting import figure
from numpy.random import random

N = 300 
source = ColumnDataSource(data={'x': random(N), 'y': random(N)})

plot = figure()
plot.circle(x= 'x', y= 'y', source=source)

slider = Slider(start=100, end=1000, value=N, step=10, title= 'Number of points')


def callback(attr, old, new):
    N = slider.value
    source.data={'x': random(N), 'y': random(N)}

slider.on_change('value', callback)

layout = column(widgetbox(slider), plot)

curdoc().add_root(layout)