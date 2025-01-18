from timer import timer
from collections import Counter
import string
import random
from memory_profiler import profile

@timer
@profile
def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


@timer
@profile
def isAnagramTwo(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)

@timer
@profile
def isAnagramThree(s: str, t: str) -> bool:
    count = [0]*26
    for char in s:
        count[ord(char) - ord('a')] += 1
    for char in t:
        count[ord(char) - ord('a')] -= 1
    return count.count(0) == 26

@timer
@profile
def isAnagramFour(s: str, t: str) -> bool:
    count = Counter()
    for char in s:
        count[char] += 1
    for char in t:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] == 0:
            del count[char]
    return len(count) == 0

if __name__ == "__main__":
    s = list(string.ascii_lowercase) * 10000
    LENGTH = 10000 * 26
    random.shuffle(s)
    t = s[:]
    random.shuffle(t)
    s, t = "".join(s), "".join(t)

    print(f"\n *** Length of the string: {LENGTH} ***\n")

    print("\nSorted function")
    isAnagram(s, t)

    print("\nCounter from collections")
    isAnagramTwo(s, t)

    print("\nCount array for letters")
    isAnagramThree(s, t)

    print("\nCount dictionary for letters")
    isAnagramFour(s, t)