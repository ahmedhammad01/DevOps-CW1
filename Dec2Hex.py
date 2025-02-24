import sys

def decimal_to_hex(decimal_value):
    hex_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    hexadecimal = ""
    num = decimal_value

    print(f"Converting the Decimal Value {num} to Hex...")

    while num != 0:
        rem = num % 16
        hexadecimal = hex_chars[rem] + hexadecimal
        num //= 16

    print(f"Hexadecimal representation is: {hexadecimal}")
    return hexadecimal  # Return for testing

if __name__ == "__main__":
    # Check if an input argument is provided
    if len(sys.argv) < 2:
        print("Error: No input provided.")
        sys.exit(1)  # Exit with error code 1

    try:
        # Convert input to integer
        decimal_value = int(sys.argv[1])
        hex_result = decimal_to_hex(decimal_value)
        print(f"Hexadecimal representation is: {hex_result}")
    except ValueError:
        # Handle non-integer input
        print("Error: Invalid integer input.")
        sys.exit(1)  # Exit with error code 1
