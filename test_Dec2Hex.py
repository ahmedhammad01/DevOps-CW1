import unittest
import subprocess
import os

class TestDecimalToHex(unittest.TestCase):

    def setUp(self):
        self.script_path = os.path.join(os.path.dirname(__file__), "Dec2Hex.py")

    def test_no_input_provided(self):
        result = subprocess.run(["python3", self.script_path], capture_output=True, text=True)
        self.assertIn("Warning: No input provided. Please enter a number.", result.stdout)

    def test_non_integer_input(self):
        result = subprocess.run(["python3", self.script_path, "abc"], capture_output=True, text=True)
        self.assertIn("Error: Invalid input. Please enter an integer.", result.stdout)

    def test_negative_input(self):
        result = subprocess.run(["python3", self.script_path, "-5"], capture_output=True, text=True)
        self.assertIn("Error: Invalid input. Input must be non-negative.", result.stdout)
        self.assertEqual(result.returncode, 0)

    def test_valid_input(self):
        result = subprocess.run(["python3", self.script_path, "15"], capture_output=True, text=True)
        self.assertIn("Hexadecimal representation is: F", result.stdout)

if __name__ == "__main__":
    unittest.main()
