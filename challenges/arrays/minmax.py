# Find the largest and the smallest number in a given array.
from typing import List

def minmax(nums: List[int]) -> List[int]:
    min_value = float('inf')
    max_value = float('-inf')
    for num in nums:
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num
    return [min_value, max_value] if len(nums) != 0 else []


def main():
    try:
        min_value, max_value = minmax([1, 2, 3, 4])
        print(f"Min: {min_value}\tMax: {max_value}")
    except:
        print("Invalid input")


if __name__ == "__main__":
    main()