def containsDuplicate(s: str) -> bool:
    # Maintain a set
    unique: set[chr] = set()
    for letter in s:
        if letter in unique:
            return True
        unique.add(letter)
    return False


def main() -> None:
    s: str = "abcdefghijklmnopqrstuvwxyz"
    retVal: bool = containsDuplicate(s)
    print(retVal)

    s: str = "aabbc"
    retVal: bool = containsDuplicate(s)
    print(retVal)


if __name__ == "__main__":
    main()