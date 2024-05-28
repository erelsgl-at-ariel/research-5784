"""
Demo 2: Passing functions as arguments.
"""


def algorithm_A(x, y, z):
    return 2*(x+y+z)

def algorithm_B(x, y, z):
    return 3*(x+y+z)

def adder(algorithm, x, y, z):
    return {"sum": algorithm(x,y,z)}


import experiments_csv, logging
ex = experiments_csv.Experiment("results/", "demo2.csv", backup_folder=None)
ex.logger.setLevel(logging.DEBUG)

input_ranges = {
    "x": [1,2,3],
    "y": [4,5],
    "z": [6],
    "algorithm": [algorithm_A, algorithm_B]
}
ex.run(adder, input_ranges)
