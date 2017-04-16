#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 10:49:59 2017

@author: jerry
"""
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.sampledata.iris import flowers as df
from bokeh.models import ColumnDataSource, CategoricalColorMapper, HoverTool

source = ColumnDataSource(df)

mapper = CategoricalColorMapper(factors=['setosa', 'virginica', 'versicolor'],
                                palette=['red', 'green', 'blue'])

hover = HoverTool(tooltips=[
        ('species name', '@species'),
        ('petal length', '@petal_length'),
        ('sepal length', '@sepal_length')
        ])

p = figure(x_axis_label='petal_length',
           y_axis_label='sepal_length',
           tools=[hover, 'pan', 'wheel_zoom'])

p.circle('petal_length',
         'sepal_length',
         source=source,
         size=10,
         color={'field':'species', 'transform':mapper},
        legend='species')

p.legend.location = 'top_left'

output_file('annotations.html')
show(p)

