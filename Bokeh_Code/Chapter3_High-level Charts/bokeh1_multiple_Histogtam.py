#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 00:00:05 2017

@author: jerry
"""

from bokeh.charts import Histogram, output_file, show
from bokeh.sampledata.iris import flowers as df

p = Histogram(df, 'petal_length',
              color='species', title='Iris')

output_file('histogram.html')
show(p)


