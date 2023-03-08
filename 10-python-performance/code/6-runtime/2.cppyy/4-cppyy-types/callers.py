#!python3

import cppyy
cppyy.include("functions.hpp")

print("\nCall a C++ function that expects a std::vector:")
print(cppyy.gbl.sum([1,2,3,4,5,6,7,8,9,10]))
print(cppyy.gbl.sum(range(1,12)))
# print(cppyy.gbl.sum([[1,2,3],[4,5,6],[7,8,9,10]]))
print(cppyy.gbl.sum.__doc__)

print("\nCall a C++ function that expects a std::set:")
print(cppyy.gbl.sumset({1,2,3,4,5}))

# If the above yields a compile error, we have to explicitly create a C++ set (not a Python set).
# See https://stackoverflow.com/a/56350681/827927
# cppset = cppyy.gbl.std.set[int]()
# for i in range(1,6):
# 	cppset.insert(i)
# print(cppyy.gbl.sumset(cppset)) 
print(cppyy.gbl.sumset.__doc__)


print("\nCall a C++ function that expects a std::map:")
print(cppyy.gbl.summap({1:9, 2:8, 3:7}))
print(cppyy.gbl.summap.__doc__)
