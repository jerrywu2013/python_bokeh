#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 12:00:04 2017

@author: jerry
"""

from bokeh.models import ColumnDataSource
from bokeh.sampledata.iris import flowers as df

print(df.head())
source = ColumnDataSource(df)

print(source)


##############################

from bokeh.plotting import ColumnDataSource

source = ColumnDataSource(df)

p.circle(x='Year',
         y='Time',
         color='color',
         source=source,
         size=8)

output_file('sprint.html')
show(p)
