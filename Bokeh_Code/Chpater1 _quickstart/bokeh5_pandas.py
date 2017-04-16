#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 11:25:04 2017

@author: jerry
"""
from bokeh.io import output_file,show
from bokeh.plotting import figure
from bokeh.sampledata.iris import flowers

plot =figure()

plot.circle(flowers['petal_length'],
            flowers['sepal_length'],
            size=10)

output_file('pandas.html')
show(plot)