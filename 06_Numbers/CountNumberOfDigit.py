"""
In any loop, if the number of iterations depends on a number and that number educes by a factor
(like dividing 2, 3, etc.) in each step, then the time complexity is O(log (N))

"""

# TC = O(log 10 (n))
# SC = O(1)


def CountNumberOfDigit(n):
    num = n
    count = 0

    while num > 0:
        count += 1
        num = num // 10

    return count


"""
Note : If we take the log base 10 of any number and add 1 to it,
then convert it to an integer, we can find the number of digit in that number

"""

import math


def CountNumberOfDigitUsingMath(n):
    num = n
    return int(math.log10(num) + 1)


if __name__ == "__main__":
    n = 45638

    print(CountNumberOfDigit(n))
    print(CountNumberOfDigitUsingMath(n))
