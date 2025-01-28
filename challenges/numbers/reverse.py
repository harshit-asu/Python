# Reverse an integer.

def reverse(number: int) -> int:
    return int(str(number)[::-1])

def main():
    print(reverse(143))
    print(reverse(1439810))
    print(reverse(1430987))

if __name__ == "__main__":
    main()