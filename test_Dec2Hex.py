import unittest
import subprocess

class TestDecimalToHex(unittest.TestCase):

    def test_valid_input(self):
        self.assertEqual(subprocess.run(["python3", "Dec2Hex.py", "15"], capture_output=True, text=True).stdout.strip(),
                         "Hexadecimal representation is: F")
        self.assertEqual(subprocess.run(["python3", "Dec2Hex.py", "255"], capture_output=True, text=True).stdout.strip(),
                         "Hexadecimal representation is: FF")

    def test_zero_input(self):
        result = subprocess.run(["python3", "Dec2Hex.py", "0"], capture_output=True, text=True)
        self.assertIn("Hexadecimal representation is: 0", result.stdout)

    def test_no_input_provided(self):
        result = subprocess.run(["python3", "Dec2Hex.py"], capture_output=True, text=True)
        self.assertIn("Warning: No input provided. Please enter a number.", result.stdout)

    def test_non_integer_input(self):
        result = subprocess.run(["python3", "Dec2Hex.py", "abc"], capture_output=True, text=True)
        self.assertIn("Error: Invalid input. Please enter an integer.", result.stdout)

    def test_negative_input(self):
        result = subprocess.run(["python3", "Dec2Hex.py", "-5"], capture_output=True, text=True)
        self.assertIn("Error: Please enter a non-negative integer.", result.stdout)

if __name__ == "__main__":
    unittest.main()
