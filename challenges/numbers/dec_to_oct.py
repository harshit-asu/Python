"""
Convert decimal numbers to octal numbers.
"""

def dec_to_oct(number: int) -> int:
    result = ""
    while number:
        rem = number % 8
        result += str(rem)
        number //= 8
    return int(result[::-1])

def main():
    print(dec_to_oct(1729))

if __name__ == "__main__":
    main()