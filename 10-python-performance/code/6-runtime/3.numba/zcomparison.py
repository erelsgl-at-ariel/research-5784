from numba import njit, vectorize, int32, int64
from functools import wraps
from time import perf_counter

def my_timer(orig_func):
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = perf_counter()
        result = orig_func(*args, **kwargs)
        t2 = perf_counter() - t1
        print(f'{ orig_func.__name__} ran in: { t2} sec')
        return result
    return wrapper

@my_timer
def func(max_x,max_y,max_z):
    lst = []
    for x in range(max_x):
        for y in range(max_y):
            for z in range(max_z):
                if (z + x + y)/10 == x:
                    lst.append(x)
    return lst

@my_timer
@njit
def njit_func(max_x,max_y,max_z):
    lst = []
    for x in range(max_x):
        for y in range(max_y):
            for z in range(max_z):
                if (z + x + y)/10 == x:
                    lst.append(x)
    return lst

max_x = 10
max_y = 10
max_z = 10
print(f'x = {max_x} , y = {max_y} , z= {max_z}')
func(max_x,max_y,max_z)
njit_func(max_x,max_y,max_z)

max_y = 1000
max_z = 1000
print(f'\nx = {max_x} , y = {max_y} , z= {max_z}')
func(max_x,max_y,max_z)
njit_func(max_x,max_y,max_z)

max_z = 10000
print(f'\nx = {max_x} , y = {max_y} , z= {max_z}')
func(max_x,max_y,max_z)
njit_func(max_x,max_y,max_z)


