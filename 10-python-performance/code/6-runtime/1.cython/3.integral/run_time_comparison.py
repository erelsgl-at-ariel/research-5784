import timeit

cy = timeit.timeit('cy_integrate.integrate(20,30,10000)',
                    setup='import cy_integrate',
                    number = 1000 )

py = timeit.timeit('py_integrate.integrate(20,30,10000)',
                    setup='import py_integrate',
                    number = 1000 )

print(f'cy = {cy}')
print(f'py = {py}')
print(f'Cython is {py/cy} times faster')
