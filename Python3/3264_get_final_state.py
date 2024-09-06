from typing import List


def getFinalState(nums: List[int], k: int, multiplier: int) -> List[int]:
    for _ in range(k):
        x = min(nums)
        nums[nums.index(x)] = x * multiplier
    return nums


def test_getFinalState_example_1():
    nums = [2, 1, 3, 5, 6]
    k = 5
    multiplier = 2
    assert getFinalState(nums, k, multiplier) == [8, 4, 6, 5, 6]


def test_getFinalState_example_2():
    nums = [1, 2]
    k = 3
    multiplier = 4
    assert getFinalState(nums, k, multiplier) == [16, 8]


def main():
    result = getFinalState([1, 2], k=3, multiplier=4)


if __name__ == "__main__":
    main()
