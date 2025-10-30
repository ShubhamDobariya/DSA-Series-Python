# TC = O(2ⁿ)
# SC = O(n)


def FibonacciNum(num):
    # Base case
    if num == 0 or num == 1:
        return num

    return FibonacciNum(num - 1) + FibonacciNum(num - 2)


if __name__ == "__main__":
    num = 7

    print(FibonacciNum(num))
