import sys

HEX_BASE = 16
HEX_CHARS = "0123456789ABCDEF"

def decimal_to_hex(decimal_value):
    """Convert a decimal number to hexadecimal representation."""
    if decimal_value == 0:
        return "0"
    hexadecimal = ""
    num = decimal_value
    while num > 0:
        rem = num % HEX_BASE
        hexadecimal = HEX_CHARS[rem] + hexadecimal
        num //= HEX_BASE
    return hexadecimal

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Warning: No input provided. Please enter a number.")
        sys.exit(0)  # Do not fail the Jenkins build for missing input
    
    try:
        decimal_value = int(sys.argv[1])
        if decimal_value < 0:
            print("Error: Please enter a non-negative integer.")
            sys.exit(1)  # Jenkins should fail if the input is invalid
        hex_result = decimal_to_hex(decimal_value)
        print(f"Hexadecimal representation is: {hex_result}")
    except ValueError:
        print("Error: Invalid input. Please enter an integer.")
        sys.exit(0)  # Do not fail the Jenkins build for invalid input
