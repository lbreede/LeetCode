def myAtoi(s: str) -> int:
    s = s.lstrip()
    if not s:
        return 0
    sign = "+"
    if s[0] in {"-", "+"}:
        sign = s[0]
        s = s[1:]
    num = ""
    for c in s:
        if c.isdigit():
            num += c
        else:
            break
    num = int(sign + num) if num else 0

    if num < -(2**31):
        return -(2**31)

    if num > 2**31 - 1:
        return 2**31 - 1

    return num


def main() -> None:
    assert myAtoi("42") == 42
    assert myAtoi("   -42") == -42
    assert myAtoi("4193 with words") == 4193
    assert myAtoi("words and 987") == 0
    assert myAtoi("1 and 2") == 1
    assert myAtoi("-91283472332") == -2147483648


if __name__ == "__main__":
    main()
