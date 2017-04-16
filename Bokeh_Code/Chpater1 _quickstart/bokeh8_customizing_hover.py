#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 10:49:59 2017

@author: jerry
"""
from bokeh.io import output_file, show
from bokeh.models import HoverTool
from bokeh.sampledata.iris import flowers as df

source = ColumnDataSource(df)

plot = figure(tools='box_select, lasso_select')
hover = HoverTool(tooltips=None, mode='hline')

plot = figure(tools=[hover, 'crosshair'])

plot.circle(x='petal_length',
            y='sepal_length',
            source=source,
            size=15,
            hover_color='red')

output_file('iris_customizing.html')
show(plot)

