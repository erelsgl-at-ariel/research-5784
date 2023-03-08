from numba import vectorize, float64

@vectorize([float64(float64, float64)])
def f(x, y):
    return x + y

print(f([1,2,3],[4,5,6]))   # result is a vector of float64



from numba import int32,int64, float32

@vectorize([int32(int32, int32),
            int64(int64, int64),
            float32(float32, float32),
            float64(float64, float64)])
def f2(x, y):
    return x + y


print(f2([1,2,3],[4,5,6]))  # result is a vector of int32
