import unittest
import subprocess
import os

class TestDecimalToHex(unittest.TestCase):

    def setUp(self):
        # Explicit absolute path to the Dec2Hex.py file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.script_path = os.path.join(current_dir, "Dec2Hex.py")

    def test_no_input_provided(self):
        """Test case for no input provided."""
        result = subprocess.run(
            ["python3", self.script_path],
            capture_output=True, text=True, cwd=os.path.dirname(self.script_path)
        )
        self.assertIn("Warning: No input provided. Please enter a number.", result.stdout.strip())

    def test_non_integer_input(self):
        result = subprocess.run(
            ["python3", self.script_path, "abc"],
            capture_output=True, text=True, cwd=os.path.dirname(self.script_path)
        )
        self.assertIn("Error: Invalid input. Please enter an integer.", result.stdout.strip())

    def test_negative_input(self):
        result = subprocess.run(
            ["python3", self.script_path, "-5"],
            capture_output=True, text=True, cwd=os.path.dirname(self.script_path)
        )
        self.assertIn("Error: Please enter a non-negative integer.", result.stdout.strip())
        self.assertEqual(result.returncode, 1)

    def test_valid_input(self):
        result = subprocess.run(
            ["python3", self.script_path, "15"],
            capture_output=True, text=True, cwd=os.path.dirname(self.script_path)
        )
        self.assertIn("Hexadecimal representation is: F", result.stdout.strip())

    @property
    def script_path(self):
        # Explicitly locate the script relative to test file location
        return os.path.abspath(os.path.join(os.path.dirname(__file__), "Dec2Hex.py"))

if __name__ == "__main__":
    unittest.main()
