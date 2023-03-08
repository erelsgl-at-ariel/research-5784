from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("hello.pyx")
)


# To compile, run the following command:
#      pip install cython
#      python setup.py build_ext --inplace
# This should create the following files:
#      hello.c
#      hello.*.pyd [on Windows]
#      hello.so    [on Linux]
