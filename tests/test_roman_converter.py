import unittest
import sys
import os

# para importar correctamente desde src/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from roman_converter import decimal_to_roman

class TestRomanConverter(unittest.TestCase):

    def test_basicos(self):
        self.assertEqual(decimal_to_roman(1), "I")
        self.assertEqual(decimal_to_roman(3), "III")
        self.assertEqual(decimal_to_roman(5), "V")
        self.assertEqual(decimal_to_roman(10), "X")

    def test_sustraccion(self):
        self.assertEqual(decimal_to_roman(4), "IV")
        self.assertEqual(decimal_to_roman(9), "IX")
        self.assertEqual(decimal_to_roman(40), "XL")
        self.assertEqual(decimal_to_roman(90), "XC")
        self.assertEqual(decimal_to_roman(400), "CD")
        self.assertEqual(decimal_to_roman(900), "CM")

    def test_complejos(self):
        self.assertEqual(decimal_to_roman(15), "XV")
        self.assertEqual(decimal_to_roman(49), "XLIX")
        self.assertEqual(decimal_to_roman(399), "CCCXCIX")
        self.assertEqual(decimal_to_roman(944), "CMXLIV")
        self.assertEqual(decimal_to_roman(1987), "MCMLXXXVII")
        self.assertEqual(decimal_to_roman(2024), "MMXXIV")
        self.assertEqual(decimal_to_roman(3999), "MMMCMXCIX")

if __name__ == '__main__':
    unittest.main()
