# TC = O(log 10 (n))
# SC = O(1)


def PalindromeNumber(n):
    num = n
    result = 0

    while num > 0:
        last_digit = num % 10
        result = result * 10 + last_digit
        num = num // 10

    if n == result:
        print(f"{n} is Palindrome.")
    else:
        print(f"{n} is Not Palindrome.")


if __name__ == "__main__":
    n = 12321

    PalindromeNumber(n)
