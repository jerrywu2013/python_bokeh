#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 00:00:05 2017

@author: jerry
"""

from bokeh.charts import BoxPlot, output_file, show
from bokeh.sampledata.iris import flowers as df

p = BoxPlot(df, values='petal_length',
              label='species', color='species',
              title='Iris')

p.yaxis.axis_label = 'Petal_length (% population)'

output_file('BoxPlot.html')
show(p)


