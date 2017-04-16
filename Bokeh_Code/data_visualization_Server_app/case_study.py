#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
Created on Mon Apr  3 09:22:59 2017

@author: jerry
"""

##################################

from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.models import HoverTool, ColumnDataSource
import pandas as pd

df = pd.read_csv('gapminder.csv', index_col='year')


source = ColumnDataSource(data={
    'x'       : df.loc[2007].gdpPercap,
    'y'       : df.loc[2007].lifeExp,
    'country' : df.loc[2007].country
})


p = figure(title='2007',
           x_axis_label='GDP(Per Cap)',
           y_axis_label='Life Expectancy (years)',
           plot_height=400, plot_width=700,
           tools=[HoverTool(tooltips='@country')])


p.circle(x='x', y='y', source=source)


output_file('gapminder.html')
show(p)