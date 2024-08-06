"""
Demo 7: plotting experiment results; multiple subplots.
"""

from experiments_csv import *
from matplotlib import pyplot as plt

multi_plot_results("results/demo1.csv", filter={}, subplot_rows=2, subplot_cols=2,
    x_field="x", y_field="sum", z_field="y", subplot_field="z", mean=True)
    # Should show two-by-two subplots.

multi_plot_results("results/demo1.csv", filter={}, subplot_rows=2, subplot_cols=2,
    x_field="x", y_field="sum", z_field="y", subplot_field="z", 
    sharex=True, sharey=True, mean=True)
    # Should show two-by-two subplots.

multi_plot_results("results/demo1.csv", filter={}, subplot_rows=2, subplot_cols=2,
    x_field="x", y_field="sum", z_field="y", subplot_field="z", 
    sharex=True, sharey=True, mean=True, save_to_file="results/demo1_multiplot.png")
    # Should save the last plot to file "results/demo1.png"
