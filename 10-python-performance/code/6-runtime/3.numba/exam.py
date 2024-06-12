import numpy as np
from time import perf_counter

x = np.arange(1000000).reshape(1000, 1000)

def go_fast(a): 
    sumtanh = 0.0
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            sumtanh += np.tanh(a[i, j])
    return a + sumtanh

start = perf_counter()
go_fast(x)
end = perf_counter()
print(f"Elapsed (first time) = {end - start}")

start = perf_counter()
go_fast(x)
end = perf_counter()
print(f"Elapsed (second time) = {end - start}")
