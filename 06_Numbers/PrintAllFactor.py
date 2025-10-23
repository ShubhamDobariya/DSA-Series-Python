"""
Brute Force Solution

TC = O(N)
SC = O(K) where k would the number of factor

"""


def BruteForcePrintAllFactor(n):
    num = n
    result = []

    for i in range(1, num + 1):
        if num % i == 0:
            result.append(i)

    return result


"""
Better Solution

TC = O(N/2) = O(N + 1/2) = O(N)
SC = O(K) where k would the number of factor

"""


def BetterPrintAllFactor(n):
    num = n
    result = []

    for i in range(1, int((num / 2) + 1)):
        if num % i == 0:
            result.append(i)

    result.append(num)

    return result


"""
Optimal Solution 

TC = O(sqrt(N) + O(N log N))
SC = O(K) where k would the number of factor

"""
from math import sqrt


def OptimalPrintAllFactor(n):
    num = n
    result = []

    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:
            result.append(i)

            if num // i != i:
                result.append(num // i)

    result.sort()
    return result


if __name__ == "__main__":
    n = 20

    print(BruteForcePrintAllFactor(n))
    print(BetterPrintAllFactor(n))
    print(OptimalPrintAllFactor(n))
