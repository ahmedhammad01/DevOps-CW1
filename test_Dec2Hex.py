import unittest
import subprocess

class TestDecimalToHex(unittest.TestCase):
    
    def test_no_input_provided(self):
        """Test case for no input provided."""
        result = subprocess.run(["python3", "Dec2Hex.py"], capture_output=True, text=True)
        self.assertIn("Warning: No input provided. Please enter a number.", result.stdout)

    def test_non_integer_input(self):
        """Test case for non-integer input."""
        result = subprocess.run(["python3", "Dec2Hex.py", "abc"], capture_output=True, text=True)
        self.assertIn("Error: Invalid input. Please enter an integer.", result.stdout)

if __name__ == "__main__":
    unittest.main()
