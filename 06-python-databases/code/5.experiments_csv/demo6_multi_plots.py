"""
Demo 6: plotting experiment results; multiple subplots.
"""

from experiments_csv import *
from matplotlib import pyplot as plt

multi_plot_results("../examples/results/demo1.csv", filter={}, subplot_field="z", subplot_rows=2, subplot_cols=2,
    x_field="x", y_field="sum", z_field="y", mean=True)
    # Should show two-by-two subplots.

multi_plot_results("../examples/results/demo1.csv", filter={}, subplot_field="z", subplot_rows=2, subplot_cols=2,
    x_field="x", y_field="sum", z_field="y", sharex=True, sharey=True, mean=True)
    # Should show two-by-two subplots.

multi_plot_results("../examples/results/demo1.csv", filter={}, subplot_field="z", subplot_rows=2, subplot_cols=2,
    x_field="x", y_field="sum", z_field="y", sharex=True, sharey=True, mean=True, save_to_file=True)
    # Should save the last plot to file "results/demo1.png"
