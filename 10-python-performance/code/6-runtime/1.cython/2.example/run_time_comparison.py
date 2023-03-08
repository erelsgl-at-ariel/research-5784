import timeit  # Check performance of functions by running them many times

cy = timeit.timeit('cy_example.sum_of_ints(500)',
                    setup='import cy_example',
                    number = 100000 )

py = timeit.timeit('py_example.sum_of_ints(500)',
                    setup='import py_example',
                    number = 100000 )

print(f'cy = {cy}')
print(f'py = {py}')
print(f'Cython is {py/cy} times faster')
