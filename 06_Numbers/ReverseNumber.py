# TC = O(log 10 (n))
# SC = O(1)


def ReverseNumber(n):
    num = n
    reverseNum = 0

    while num > 0:
        last_digit = num % 10
        reverseNum = reverseNum * 10 + last_digit
        num = num // 10

    return reverseNum


if __name__ == "__main__":
    n = 12345

    print(ReverseNumber(n))
