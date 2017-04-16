from bokeh.io import output_file, show 
from bokeh.plotting import figure
plot = figure(plot_width=400,
              tools='pan,box_zoom',
              y_axis_label='new',
              x_axis_label='new2')
#plot.circle([1,2,3,4,5],[8,6,5,2,3])
plot.circle(x=10, y=[2,5,8,12], size=[10,20,30,40])
output_file('circle.html')
show(plot)





