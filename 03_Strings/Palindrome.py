# TC = O(N/2) = O(N)
# SC = O(1)


def PalindromeStr(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    s = "nitin"

    print(PalindromeStr(s))
