import sys
import pandas as pd

def print_size(number: int):
    print(f"The number {number} occupies {sys.getsizeof(number)} bytes.")
    return sys.getsizeof(number)


if __name__ == "__main__":
    numbers = [10**i for i in range(20)]
    data = []
    for i, number in enumerate(numbers):
        print(f"{i}: ", end="")
        data.append([i, print_size(number)])
    df = pd.DataFrame(data, columns=["Power", "Size"])
    print("\nThe size of 'int' object for different powers of 10 (0 to 19)\n")
    print(df)

    print(f"\nMaximum size on my machine - {sys.maxsize}")