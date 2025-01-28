"""
Write a function in Python to parse a string such that it accepts a parameter- an encoded string.
This encoded string will contain a first name, last name, and an id. You can separate the values in the
string by any number of zeros. The id will not contain any zeros.
The function should return a Python dictionary with the first name, last name, and id values.
For example, if the input would be “John000Doe000123”. Then the function should return:
{ “first_name”: “John”, “last_name”: “Doe”, “id”: “123” }
"""

def decode(encoded_str: str) -> dict:
    values = list()
    curr = ""
    for char in encoded_str:
        if char == "0" and curr != "":
            values.append(curr)
            curr = ""
        elif char != "0":
            curr += char
    if curr != "":
        values.append(curr)
    decoded = {
        "first_name": values[0],
        "last_name": values[1],
        "id": values[2]
    }
    return decoded


def main():
    encoded_str = "John000Doe000123"
    print(decode(encoded_str))


if __name__ == "__main__":
    main()