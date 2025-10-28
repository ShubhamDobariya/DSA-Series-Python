# TC = O(N)
# SC = O(N) due to recursion stack


def Factorial(num):
    ## Base Case
    ## Factorial of 0 and 1 => 1
    if num == 0 or num == 1:
        return 1

    return num * Factorial(num - 1)


if __name__ == "__main__":
    num = 5

    print(Factorial(num))
