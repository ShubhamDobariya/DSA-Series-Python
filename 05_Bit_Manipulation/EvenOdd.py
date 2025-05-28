# Check if a number is even or odd
# All even numbers end in 0 and odd numbers end in 1 in binary

"""
        AND (&)
0   0   -->     0
1   0   -->     0
0   1   -->     0
1   1   -->     1
"""


def is_even(nums):
    return (nums & 1) == 0


if __name__ == "__main__":
    num = 10

    print(is_even(num))
