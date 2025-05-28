# Swap two numbers without temp

"""
        XOR (^)
0   0   -->     0
1   0   -->     1
0   1   -->     1
1   1   -->     0
"""


def swapTwoNumberWithoutTemp(n1, n2):
    n1 ^= n2
    n2 ^= n1
    n1 ^= n2

    return (n1, n2)


if __name__ == "__main__":
    n1 = 10
    n2 = 20

    print(swapTwoNumberWithoutTemp(n1, n2))
