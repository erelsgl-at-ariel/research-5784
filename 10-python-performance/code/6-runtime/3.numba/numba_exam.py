from numba import jit
import numpy as np
from time import perf_counter

x = np.arange(1000000).reshape(1000, 1000)

@jit(nopython=True)  
# nopython means that the python interpreter is not used in compiling 
# this function. It is faster, but might not know some Python objects.
def go_fast(a): # Function is compiled and runs in machine code
    sumtanh = 0.0
    for i in range(a.shape[0]):
        sumtanh += np.tanh(a[i, i])
    return a + sumtanh

# DO NOT REPORT THIS... COMPILATION TIME IS INCLUDED IN THE EXECUTION TIME!
start = perf_counter()
go_fast(x)
end = perf_counter()
print("Elapsed (with compilation) = %s" % (end - start))

# NOW THE FUNCTION IS COMPILED, RE-TIME IT EXECUTING FROM CACHE
start = perf_counter()
go_fast(x)
end = perf_counter()
print("Elapsed (after compilation) = %s" % (end - start))
