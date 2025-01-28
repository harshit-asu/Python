"""
Write a function in Python to convert a decimal to a hex.
It must accept a string of ASCII characters as input.
The function should return the value of each character as a hexadecimal string.
You have to separate each byte by a space and return all alpha hexadecimal characters as lowercase.
"""

def string_to_hex(input_str: str) -> str:
    hex_values = []
    for char in input_str:
        hex_values.append(hex(ord(char))[2:].lower())
    return " ".join(hex_values)


def main():
    print(string_to_hex("harshit_allumolu"))


if __name__ == "__main__":
    main()