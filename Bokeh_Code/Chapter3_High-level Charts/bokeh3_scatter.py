#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 00:00:05 2017

@author: jerry
"""

from bokeh.charts import Scatter, output_file, show
from bokeh.sampledata.iris import flowers as df

p = Scatter(df, x='petal_length', y='sepal_length',
            marker='species', color='species', title='Iris')

output_file('Scatter.html')
show(p)


