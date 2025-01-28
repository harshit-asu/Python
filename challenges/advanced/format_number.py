"""
Write a function named format_number that takes a non-negative number as its only parameter.
Your function should convert the number to a string and add commas as a thousand separators.
For example, calling format_number(1000000) should return “1,000,000”.
"""

def format_number(number: int) -> str:
    number_str = str(number)
    ind = len(number_str) % 3
    formatted_number = number_str[:ind]
    if ind != 0 and ind < len(number_str):
        formatted_number += ","
    for i in range(ind, len(number_str), 3):
        formatted_number += number_str[i:i+3]
        if i+3 != len(number_str):
            formatted_number += ","
    return formatted_number


def main():
    print(format_number(1000))

if __name__ == "__main__":
    main()