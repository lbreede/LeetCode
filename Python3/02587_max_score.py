from itertools import accumulate


def maxScore(nums: list[int]) -> int:
    return sum(x > 0 for x in accumulate(sorted(nums, reverse=True)))


def main() -> None:
    output = maxScore([2, -1, 0, 1, -3, 3, -3])
    assert output == 6, f"Example 1 - Fail: {output}"
    print(f"Example 1 - Pass: {output}")

    output = maxScore([-2, -3, 0])
    assert output == 0, f"Example 2 - Fail: {output}"
    print(f"Example 2 - Pass: {output}")


if __name__ == "__main__":
    main()
