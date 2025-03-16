import unittest
import subprocess
from Dec2Hex import decimal_to_hex

class TestDecimalToHex(unittest.TestCase):

    def test_decimal_to_hex_conversion(self):
        """Test valid integer conversions."""
        self.assertEqual(decimal_to_hex(0), "0")
        self.assertEqual(decimal_to_hex(10), "A")
        self.assertEqual(decimal_to_hex(255), "FF")
        self.assertEqual(decimal_to_hex(16), "10")

    def test_no_input_provided(self):
        """Test case for no input provided."""
        result = subprocess.run(["python3", "Dec2Hex.py"], capture_output=True, text=True)
        self.assertIn("Warning: No input provided. Please enter a number.", result.stdout)
        self.assertEqual(result.returncode, 0)

    def test_non_integer_input(self):
        """Test case for non-integer input."""
        result = subprocess.run(["python3", "Dec2Hex.py", "abc"], capture_output=True, text=True)
        self.assertIn("Error: Invalid input. Please enter an integer.", result.stdout)
        self.assertEqual(result.returncode, 0)

    def test_negative_integer_input(self):
        """Test case for negative integer input."""
        result = subprocess.run(["python3", "Dec2Hex.py", "-5"], capture_output=True, text=True)
        self.assertIn("Error: Please enter a non-negative integer.", result.stdout)
        self.assertEqual(result.returncode, 1)

if __name__ == "__main__":
    unittest.main()
