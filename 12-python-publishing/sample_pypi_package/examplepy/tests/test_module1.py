import unittest

import examplepy

from examplepy.module1 import Number

class TestSimple(unittest.TestCase):

    def test_add(self):
        print(examplepy.__version__)
        print(examplepy.__file__)
        self.assertEqual((Number(5) + Number(6)).value, 11)


if __name__ == '__main__':
    unittest.main()
