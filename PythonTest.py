import unittest

# funciones.py
def suma(a, b):
    return a + b
def resta(a, b):
    return a - b

# test_unittest.py
class TestFunciones(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)
        self.assertEqual(suma(-1, 1), 0)
        self.assertEqual(suma(0, 0), 0)
        self.assertEqual(suma(1.5, 2.5), 4.0)
        self.assertEqual(suma('hola', 'mundo'), 'holamundo')

    def test_resta(self):
        self.assertEqual(resta(2, 3), -1)
        self.assertEqual(resta(-1, 1), -2)
        self.assertEqual(resta(0, 0), 0)
        self.assertEqual(resta(1.5, 2.5), -1.0)
        self.assertRaises(TypeError, resta, 'hola', 'mundo')

# test_pytest.py
def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0
    assert suma(0, 0) == 0
    assert suma(1.5, 2.5) == 4.0
    assert suma('hola', 'mundo') == 'holamundo'

def test_resta():
    assert resta(2, 3) == -1
    assert resta(-1, 1) == -2
    assert resta(0, 0) == 0
    assert resta(1.5, 2.5) == -1.0
    with pytest.raises(TypeError):
        resta('hola', 'mundo')

