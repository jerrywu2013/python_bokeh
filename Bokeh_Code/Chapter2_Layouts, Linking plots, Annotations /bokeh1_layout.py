#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 16:08:39 2017

@author: jerry
"""
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.sampledata.iris import flowers as df
from bokeh.layouts import row

p1 = figure(x_axis_label='petal_length', y_axis_label='sepal_length')

p1.circle(df['petal_length'], df['sepal_length'], size=10)

p2 = figure(x_axis_label='sepal_length', y_axis_label='petal_length')

p2.circle(df['sepal_length'], df['petal_length'], size=20)


layout = row(p1, p2)
output_file('layouts.html')
show(layout)

