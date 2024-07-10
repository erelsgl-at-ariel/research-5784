import time 
import concurrent.futures
import numpy as np
WORKERS=4

def sum_list(thelist:np.array):
	return np.sum(thelist**3//10)

LISTSIZE = 20000000
big_list = np.array(range(LISTSIZE), dtype='float64')

def sequential():
    start = time.perf_counter()
    big_sum=sum_list(big_list)
    print(f"Sequential: sum={big_sum}, time={time.perf_counter()-start} sec")

def threads():
    start = time.perf_counter()
    parts = [big_list[0:LISTSIZE//4], big_list[LISTSIZE//4:LISTSIZE//2], big_list[LISTSIZE//2:3*LISTSIZE//4], big_list[3*LISTSIZE//4:LISTSIZE]]
    with concurrent.futures.ThreadPoolExecutor(max_workers=WORKERS) as executor:
        partial_results = executor.map(sum_list, parts)
        big_sum = sum(partial_results)
    print(f"{WORKERS} threads: sum={big_sum}, time={time.perf_counter()-start} sec")

def processes():
    start = time.perf_counter()
    parts = [big_list[0:LISTSIZE//4], big_list[LISTSIZE//4:LISTSIZE//2], big_list[LISTSIZE//2:3*LISTSIZE//4], big_list[3*LISTSIZE//4:LISTSIZE]]
    with concurrent.futures.ProcessPoolExecutor(max_workers=WORKERS) as executor:
        partial_results = executor.map(sum_list, parts)
        big_sum = sum(partial_results)
    print(f"{WORKERS} processes: sum={big_sum}, time={time.perf_counter()-start} sec")


if __name__ == '__main__':
    sequential()
    threads()
    processes()
