#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 10:49:59 2017

@author: jerry
"""
from bokeh.io import output_file, show
from bokeh.models import CategoricalColorMapper
from bokeh.sampledata.iris import flowers as df
from bokeh.plotting import ColumnDataSource

source = ColumnDataSource(df)

mapper = CategoricalColorMapper(factors=['setosa', 'virginica', 'versicolor'],
                                palette=['red', 'green', 'blue'])

p = figure(x_axis_label='petal_length', y_axis_label='sepal_length')


p.circle(x='petal_length',
            y='sepal_length',
            source=source,
            size=10,
            color={'field':'species', 'transform':mapper})

output_file('iris_customizing.html')
show(p)

