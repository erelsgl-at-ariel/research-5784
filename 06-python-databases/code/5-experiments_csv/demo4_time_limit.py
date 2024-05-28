"""
Demo 4: Running with a time-limit.
    The runner automatically skips instances that will probably take more than the time-limit.
"""
import time

def adder(x, y):
    time.sleep(x*y/10)
    return {"sum": x+y}

import experiments_csv, logging
ex = experiments_csv.Experiment("results/", "demo4.csv", backup_folder="results/backups")
ex.logger.setLevel(logging.DEBUG)
# ex.clear_previous_results()

input_ranges = {
    "x": [1,2,3],
    "y": [4,5,6],
}
ex.run_with_time_limit(adder, input_ranges, time_limit=0.9)
