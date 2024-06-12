#!python3

import itertools
from time import perf_counter

def count_permutations(N:int)->int:
	count=0
	for p in itertools.permutations(range(1,N+1)):
		count += 1
		# print(p)
	return count

if __name__=="__main__":
	for N in range(1,13):
		print (f"Permutations of 1..{N}:", flush=True)
		start = perf_counter()
		count = count_permutations(N) 
		end = perf_counter()
		duration_in_seconds = end-start
		print(f"  {count} permutations calculated in {duration_in_seconds} seconds", flush=True)

