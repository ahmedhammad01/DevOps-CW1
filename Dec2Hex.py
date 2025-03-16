import sys

HEX_BASE = 16
HEX_CHARS = "0123456789ABCDEF"

def decimal_to_hex(decimal_value):
    """Convert decimal number to hexadecimal."""
    if not isinstance(decimal_value, int):
        raise ValueError("Error: Invalid input. Please enter an integer.")
    if decimal_value < 0:
        raise ValueError("Error: Invalid input. Input must be non-negative.")
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
    import sys

    HEX_BASE = 16
    HEX_CHARS = "0123456789ABCDEF"

    if len(sys.argv) < 2:
        print("Warning: No input provided. Please enter a number.")
        sys.exit(0)

    try:
        decimal_value = int(sys.argv[1])
        if decimal_value < 0:
            print("Error: Invalid input. Input must be non-negative.")
            sys.exit(1)
        hex_result = decimal_to_hex(decimal_value)
        print(f"Hexadecimal representation is: {hex_result}")
    except ValueError:
        print("Error: Invalid input. Please enter an integer.")
        sys.exit(0)
