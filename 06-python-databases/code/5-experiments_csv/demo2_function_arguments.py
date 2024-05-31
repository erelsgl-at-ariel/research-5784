"""
Demo 2: Passing functions as arguments.
"""
import numpy as np

def algorithm_A(x, y, z):
    return 2*(x+y+z)

def algorithm_B(x, y, z):
    return 3*(x+y+z)

def adder(algorithm, seed, x, y, z):
    np.random.seed(seed)
    r = np.random.rand()*x
    return {"sum": algorithm(r,y,z)}


import experiments_csv, logging
ex = experiments_csv.Experiment("results/", "demo2.csv", backup_folder=None)
ex.logger.setLevel(logging.DEBUG)
ex.clear_previous_results()         # Uncomment this if you want to restart all experiments from scratch


input_ranges = {
    "x": [1,2,3],
    "y": [4,5],
    "z": [6],
    "seed": range(10),
    "algorithm": [algorithm_A, algorithm_B]
}
ex.run(adder, input_ranges)
