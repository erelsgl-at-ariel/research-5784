"""
Demo 5: demonstrates running experiments on random inputs, and averaging the results.
"""
import numpy as np

def adder(x, y):
    return {"sum": x+y}

def adder_random_input(x,y,seed):
    np.random.seed(seed)
    x = x ** np.random.random()
    return adder(x,y)


import experiments_csv, logging
ex = experiments_csv.Experiment("results/", "demo5.csv", backup_folder="results/backups")
ex.clear_previous_results()

input_ranges = {
    "x": range(20),
    "y": [5,10,15],
    "seed": range(10)
}
ex.run(adder_random_input, input_ranges)
