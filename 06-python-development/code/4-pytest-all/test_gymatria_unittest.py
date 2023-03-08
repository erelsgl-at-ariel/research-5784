import unittest
from gymatria import Gymatria

class TestGymatria(unittest.TestCase):
    def setUp(self):
        self.aba = Gymatria('אבא')
        self.ab = Gymatria('אב')
        self.efes = Gymatria('')
        self.aima = Gymatria('אמא')
        self.df_alef = Gymatria('dfא')

    def tearDown(self):
        pass

    def test_add(self):  # test functions must start with 'test_'
        self.assertEqual(self.aba + self.aima , 46)
        self.assertEqual(self.aba + Gymatria('fi') , 4)
        self.assertEqual(self.aba + self.aba , 8)
        self.assertEqual(self.aba + self.efes , 4)
        self.assertEqual( self.efes + self.efes , 0)
        self.assertEqual( self.efes + 10 , 10)
        self.assertEqual( self.df_alef + 0 , 1)
        self.assertEqual( self.aba + 5 , 9)
        self.assertEqual( self.ab + 104 , 107)
        self.assertEqual( self.ab + 3, 6 )
        self.assertEqual( self.ab + 3.3, 6 )

    def test_mul(self):
        self.assertEqual(self.aba * self.aima , 42*4)
        self.assertEqual(self.aba * Gymatria('fi') , 0)
        self.assertEqual(self.aba * self.aba , 16)
        self.assertEqual(self.aba * self.efes , 0)
        self.assertEqual( self.efes * self.efes , 0)
        self.assertEqual( self.efes * 10 , 0)
        self.assertEqual( self.df_alef * 1 , 1)
        self.assertEqual( self.aba * 5 , 20)
        self.assertEqual( self.ab * 104 , 104*3)
        self.assertEqual( self.ab * 3, 9 )
        self.assertEqual( self.ab * -3, 9 )

    def test_sub(self):
        self.assertEqual(self.aba - self.aima , 38)
        self.assertEqual(self.aba - Gymatria('fi') , 4)
        self.assertEqual(self.aba - self.aba , 0)
        self.assertEqual(self.aba - self.efes , 4)
        self.assertEqual( self.efes - self.efes , 0)
        self.assertEqual( self.efes - 10 , 10)
        self.assertEqual( self.df_alef - 0 , 1)
        self.assertEqual( self.aba - 5 , 1)
        self.assertEqual( self.ab - 107 , 104)
        self.assertEqual( self.ab - 3.4 , 0 )

    def test_raise(self):
        # First way:
        self.assertRaises(ValueError, Gymatria.get_value, None)
        # Second way:
        with self.assertRaises(ValueError):
            Gymatria.get_value()


if __name__ == '__main__':
    unittest.main()
    # Alternatively, run from the command line:
    # python -m unittest test_gymatria.py
