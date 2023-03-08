import numpy as np
import time

x = np.arange(1000000).reshape(1000, 1000)

def go_fast(a): 
    trace = 0.0
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            trace += np.tanh(a[i, j])
    return a + trace

start = time.time()
go_fast(x)
end = time.time()
print(f"Elapsed (first time) = {end - start}")

start = time.time()
go_fast(x)
end = time.time()
print(f"Elapsed (second time) = {end - start}")
