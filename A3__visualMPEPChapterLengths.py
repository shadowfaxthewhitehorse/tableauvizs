# PYTHON CODE
# visualize the chapter lengths in minutes of MPEP chapters (from PLI.edu)
#
#
from bokeh.plotting import figure, output_file, show

#
# Chapter length in seconds of the lectures on the MPEP chapters in the 0's, 1000's and 2000's
#
# 1. MPEP 100-900
# 2. MPEP 1000-1900
# 3. MPEP 2000-2900
fig = figure(title = "Chapter Lengths (MPEP 100-900, 1000's, 2000's)", plot_width = 375, plot_height = 175)
fig.hbar(y = [000,1000,2000], height = 1, left = 0, right = [31060,10680,14933], color = "Red")
output_file('bar.html')
show(fig)
