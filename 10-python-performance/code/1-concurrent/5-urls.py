import time, math
import concurrent.futures
import urllib.request
WORKERS=4

URLS = [
    "https://docs.python.org/3/library/concurrent.futures.html",
    "https://stackoverflow.com/questions/62488423/brokenprocesspool-while-running-code-in-jupyter-notebook",
    "https://en.wikisource.org/wiki/Talmud",
    "https://en.wikipedia.org/wiki/Barycentric_subdivision",
    ]

def get_url(url):
    with urllib.request.urlopen(url) as response:
        html = response.read()
    return len(html)

def sequential():
    start = time.perf_counter()
    answers = [get_url(p) for p in URLS]
    print(f"Sequential: answers={answers}, time={time.perf_counter()-start} sec")

def threads():
    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=WORKERS) as executor:
        futures = [executor.submit(get_url, p) for p in URLS] 
        answers = []
        for future in concurrent.futures.as_completed(futures):   # return each result as soon as it is completed:
            answers.append(future.result())
    print(f"{WORKERS} threads: answers={answers}, time={time.perf_counter()-start} sec")

def processes():
    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=WORKERS) as executor:
        futures = [executor.submit(get_url, p) for p in URLS] 
        answers = []
        for future in concurrent.futures.as_completed(futures):   # return each result as soon as it is completed:
            answers.append(future.result())
    print(f"{WORKERS} processes: answers={answers}, time={time.perf_counter()-start} sec")


if __name__ == '__main__':
    sequential()
    threads()
    processes()
