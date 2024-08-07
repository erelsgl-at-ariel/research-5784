import time, math
import concurrent.futures
import requests

WORKERS=4

URLS = [
    "https://docs.python.org/3/library/concurrent.futures.html",
    "https://stackoverflow.com/questions/62488423/brokenprocesspool-while-running-code-in-jupyter-notebook",
    "https://en.wikisource.org/wiki/Talmud",
    "https://en.wikipedia.org/wiki/Barycentric_subdivision",
    ]

def get_url(url):
    response = requests.get(url)
    return len(response.text)

def sequential():
    start = time.perf_counter()
    answers = [get_url(p) for p in URLS]
    print(f"Sequential: answers={list(answers)}, time={time.perf_counter()-start} sec")

def threads():
    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=WORKERS) as executor:
        answers = executor.map(get_url, URLS)
    print(f"{WORKERS} threads: answers={list(answers)}, time={time.perf_counter()-start} sec")

def processes():
    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=WORKERS) as executor:
        answers = executor.map(get_url, URLS)
    print(f"{WORKERS} processes: answers={list(answers)}, time={time.perf_counter()-start} sec")


if __name__ == '__main__':
    sequential()
    threads()
    processes()
