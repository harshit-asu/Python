from typing import List
import random
from timer import timer
from memory_profiler import profile

@timer
@profile
def containsDuplicate(nums: List[int]) -> bool:
    unique = set()
    for num in nums:
        if num in unique:
            return True
        unique.add(num)
    return False


@timer
@profile
def containsDuplicateTwo(nums: List[int]) -> bool:
    return len(set(nums)) != len(nums)


if __name__ == "__main__":
    nums = list(range(1000000))
    shuffled = nums + nums
    random.shuffle(shuffled)

    print("\nContaining Duplicate Elements\n")
    print("Set with early stopping: ")
    containsDuplicate(shuffled)

    print("\nSet with built-in method and length comparision: ")
    containsDuplicateTwo(shuffled)

    print("\nNo Duplicate Elements\n")
    print("Set with early stopping: ")
    containsDuplicate(nums)

    print("\nSet with built-in method and length comparision: ")
    containsDuplicateTwo(nums)