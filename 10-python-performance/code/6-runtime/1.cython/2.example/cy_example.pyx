cpdef int sum_of_ints(int x):   # cpdef = available both in Cython and in Python.
    cdef int y = 0              # cdef = available in Cython only.
    cdef int i = 0
    for i in range(x):
        y+=i
    return y
