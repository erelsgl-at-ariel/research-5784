import time 
import concurrent.futures
WORKERS=4

def do_something(index):
    print(f"Start {index}")
    time.sleep(1)   # simulate doing hard work
    print(f"End {index}")
    return 0


def sequential():
    start = time.perf_counter()
    do_something(1)
    do_something(2)
    print(f"Sequential: time={time.perf_counter()-start} sec")

def threads():
    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=WORKERS) as executor:
        executor.submit(do_something, 1)
        executor.submit(do_something, index=2)
    print(f"{WORKERS} threads: time={time.perf_counter()-start} sec")

def processes():
    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=WORKERS) as executor:
        executor.submit(do_something, index=1)
        executor.submit(do_something, 2)
    print(f"{WORKERS} processes: time={time.perf_counter()-start} sec")


if __name__ == '__main__':
    # sequential()
    # threads()
    processes()
