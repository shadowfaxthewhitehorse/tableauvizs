# PYTHON CODE
# visualize the chapter lengths in minutes of MPEP chapters
#
#
from bokeh.plotting import figure, output_file, show
fig = figure(title = "Chapter Lengths (MPEP 100-900, 1000's, 2000's)", plot_width = 375, plot_height = 175)
fig.hbar(y = [000,1000,2000], height = 1, left = 0, right = [31060,10680,14933], color = "Red")
output_file('bar.html')
show(fig)