from timer import timer
from itertools import product


@timer
def get_max_sum_of_triplets(nums1: list[int], nums2: list[int], nums3: list[int]) -> int:
    max_sum = float('-inf')
    for a in nums1:
        for b in nums2:
            for c in nums3:
                curr_sum = a + b + c
                if curr_sum > max_sum:
                    max_sum = curr_sum
    return max_sum

@timer
def get_max_sum_of_triplets_optimized(nums1: list[int], nums2: list[int], nums3: list[int]) -> int:
    max_sum = float('-inf')
    for a, b, c in product(nums1, nums2, nums3):
        curr_sum = a + b + c
        if curr_sum > max_sum:
            max_sum = curr_sum
    return max_sum


def main():
    nums1 = list(range(1, 251))
    nums2 = list(range(1, 251))
    nums3 = list(range(1, 251))

    ret_val = get_max_sum_of_triplets(nums1, nums2, nums3)
    print(f"Maximum sum: {ret_val}")

    ret_val = get_max_sum_of_triplets_optimized(nums1, nums2, nums3)
    print(f"Maximum sum: {ret_val}")


if __name__ == "__main__":
    main()