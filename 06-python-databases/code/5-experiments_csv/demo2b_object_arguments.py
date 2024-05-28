"""
Demo 2b: Passing objects as arguments.
"""

class classA:
    def __str__(self):
        return "ObjectA"
    def algorithm(self, x, y, z):
        return 2*(x+y+z)

class classB:
    def __str__(self):
        return "ObjectB"
    def algorithm(self, x, y, z):
        return 3*(x+y+z)

def adder(object, x, y, z):
    return {"sum": object.algorithm(x,y,z)}


import experiments_csv, logging
ex = experiments_csv.Experiment("results/", "demo2b.csv", backup_folder=None)
ex.logger.setLevel(logging.DEBUG)

input_ranges = {
    "x": [1,2,3],
    "y": [4,5],
    "z": [6],
    "object": [classA(), classB()]
}
ex.run(adder, input_ranges)
