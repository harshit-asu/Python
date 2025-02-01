from custom_timer import timer

@timer
def list_to_set(nums: list[int]) -> set[int]:
    result = set()
    for num in nums:
        result.add(num)
    return result

@timer
def list_to_set_single(nums: list[int]) -> set[int]:
    return set(nums)

def main():
    nums = list(range(1, 10000001))
    list_to_set(nums)
    list_to_set_single(nums)

if __name__ == "__main__":
    main()