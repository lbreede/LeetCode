from itertools import permutations
from typing import Optional


def twoSum(nums: list[int], target: int) -> Optional[list[int]]:
    for i, j in permutations(range(len(nums)), 2):
        if nums[i] + nums[j] == target:
            return [i, j]
    return None


def main():
    output = twoSum([2, 7, 11, 15], 9)
    assert output == [0, 1], f"Example 1 - Fail: {output}"
    print(f"Example 1 - Pass: {output}")

    output = twoSum([3, 2, 4], 6)
    assert output == [1, 2], f"Example 2 - Fail: {output}"
    print(f"Example 2 - Pass: {output}")

    output = twoSum([3, 3], 6)
    assert output == [0, 1], f"Example 3 - Fail: {output}"
    print(f"Example 3 - Pass: {output}")


if __name__ == "__main__":
    main()
