import time 
import concurrent.futures
WORKERS=2

def sum_list(thelist:list):
	s = 0
	for x in thelist:
		s += x**3//10
	return s

LISTSIZE = 10000000
big_list = list(range(LISTSIZE))

def sequential():
    start = time.perf_counter()
    big_sum=sum_list(big_list)
    print(f"Sequential: sum={big_sum}, time={time.perf_counter()-start} sec")

def threads():
    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=WORKERS) as executor:
        future_sum1 = executor.submit(sum_list, big_list[0:LISTSIZE//2])
        future_sum2 = executor.submit(sum_list, big_list[LISTSIZE//2:LISTSIZE])
        big_sum = 0
        for future in concurrent.futures.as_completed([future_sum1, future_sum2]):   # return each result as soon as it is completed:
            r = future.result()
            print("Partial sum: ", r)
            big_sum += r
    print(f"{WORKERS} threads: sum={big_sum}, time={time.perf_counter()-start} sec")

def processes():
    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=WORKERS) as executor:
        future_sum1 = executor.submit(sum_list, big_list[0:LISTSIZE//2])
        future_sum2 = executor.submit(sum_list, big_list[LISTSIZE//2:LISTSIZE])
        big_sum = 0
        for future in concurrent.futures.as_completed([future_sum1, future_sum2]):   # return each result as soon as it is completed:
            r = future.result()
            print("Partial sum: ", r)
            big_sum += r
    print(f"{WORKERS} processes: sum={big_sum}, time={time.perf_counter()-start} sec")


if __name__ == '__main__':
    sequential()
    threads()
    processes()
