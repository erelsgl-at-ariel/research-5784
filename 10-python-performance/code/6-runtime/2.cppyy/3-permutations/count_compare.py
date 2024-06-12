#!python3

from time import perf_counter

import count_permutations

import cppyy
cppyy.include("count_permutations.cpp")

use_cpp = True

if use_cpp:
	print("Using C++ implementation")
else:
	print("Using Python implementation")

for N in range(5,13):
	print ("Permutations of 1..{}:".format(N), flush=True)
	start = perf_counter()
	if use_cpp:
		count = cppyy.gbl.count_permutations(N)
	else:
		count = count_permutations.count_permutations(N) 
	end = perf_counter()
	duration_in_seconds = end-start
	print(f"  {count} permutations calculated in {duration_in_seconds} seconds", flush=True)
