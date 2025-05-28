# Is Power of Two
# Note : A power of two has only one bit set
"""
1 = 0001
2 = 0010
4 = 0100
8 = 1000
"""


def isPowerOfTwo(n):
    return n > 0 & (n & (n - 1)) == 0


if __name__ == "__main__":
    n = 16

    print(isPowerOfTwo(n))
