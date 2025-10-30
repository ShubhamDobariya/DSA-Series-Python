# TC = O(N/2) = O(N)
# SC = O(1)


def PalindromeStr(s, left, right):

    if left >= right:
        return True

    if s[left] != s[right]:
        return False

    return PalindromeStr(s, left + 1, right - 1)


if __name__ == "__main__":
    s = "nitin"
    left = 0
    right = len(s) - 1

    print(PalindromeStr(s, left, right))
