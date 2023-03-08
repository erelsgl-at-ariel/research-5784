from gymatria import Gymatria

aba = Gymatria('אבא')
ab = Gymatria('אב')
efes = Gymatria('')
aima = Gymatria('אמא')
df_alef = Gymatria('dfא')

def test_add():  # test functions must start with 'test_'
    assert aba + aima == 46
    assert aba + Gymatria('fi') == 4
    assert aba + aba == 8
    assert aba + efes == 4
    assert  efes + efes == 0
    assert  efes + 10 == 10
    assert  df_alef + 0 == 1
    assert  aba + 5 == 9
    assert  ab + 104 == 107
    assert  ab + 3 == 6 
    assert  ab + 3.3 == 6 

def test_mul():
    assert aba * aima == 42*4
    assert aba * Gymatria('fi') == 0
    assert aba * aba == 16
    assert aba * efes == 0
    assert  efes * efes == 0
    assert  efes * 10 == 0
    assert  df_alef * 1 == 1
    assert  aba * 5 == 20
    assert  ab * 104 == 104*3
    assert  ab * 3 == 9 
    assert  ab * -3 == 9 

def test_sub():
    assert aba - aima == 38
    assert aba - Gymatria('fi') == 4
    assert aba - aba == 0
    assert aba - efes == 4
    assert efes - efes == 0
    assert efes - 10 == 10
    assert df_alef - 0 == 1
    assert aba - 5 == 1
    assert ab - 107 == 104
    assert ab - 3.4 == 0 

import pytest

def test_raise():
    with pytest.raises(ValueError):
        Gymatria.get_value()

# Run from the command line:
#     pytest test_gymatria.py
