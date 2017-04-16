#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 12:08:02 2017

@author: jerry
"""
import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, show

df = pd.read_csv('stock_utf8.csv', encoding = 'utf-8' )

p = figure(x_axis_label='收盤指數',
           y_axis_label='漲跌點數',
           title = '106年03月31日大盤統計資訊')

p.circle(df['Closing Index'][0:114],
         df['Gains_index'][0:114], size=10)

output_file('stock-df.html')
show(p)

