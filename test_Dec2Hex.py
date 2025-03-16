import unittest
from Dec2Hex import decimal_to_hex

class TestDecimalToHex(unittest.TestCase):

    def test_valid_integer_input(self):
        self.assertEqual(decimal_to_hex(10), "A")
        self.assertEqual(decimal_to_hex(255), "FF")

    def test_no_input_provided(self):
        with self.assertRaises(SystemExit):
            decimal_to_hex()

    def test_non_integer_input(self):
        with self.assertRaises(ValueError):
            decimal_to_hex("abc")

if __name__ == "__main__":
    unittest.main()
