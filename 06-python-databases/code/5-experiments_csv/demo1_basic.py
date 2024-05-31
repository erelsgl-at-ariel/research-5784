"""
Demo 1: Basic usage.
"""

import experiments_csv, logging

ex = experiments_csv.Experiment("results/", "demo1.csv")
ex.logger.setLevel(logging.INFO) # Show every individual experiment arguments + results.


def add_three_numbers(x, y, z):
    # This is a dummy example of a function for running an "experiment".
    # Note that it must return a dict.
    return {
        "sum": (x+y+z), 
        "product": x*y*z
    }

print("\n\nFIRST EXPERIMENT\n")
input_ranges = {
    "x": [1,2,3],
    "y": [4,5],
    "z": [6]
}
ex.clear_previous_results()         # Uncomment this if you want to restart all experiments from scratch
ex.run(add_three_numbers, input_ranges)


print("\n\nSECOND EXPERIMENT\n")
input_ranges = {
    "x": [1,2,3],
    "y": [4],
    "z": [5,6,7,8]
}
ex.run(add_three_numbers, input_ranges)   # Can you guess how many combinations will be skipped in the second experiment?

print("\n DataFrame: \n",ex.dataFrame)
