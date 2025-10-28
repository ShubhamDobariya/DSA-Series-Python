# TC = O(N)
# SC = O(N) due to recursion stack


def Print1ToN(num):
    ## Base case
    if num == 0:
        return

    # Recursive call first
    Print1ToN(num - 1)

    # Then print after returning (ascending order)
    print(num)


## Reverse Order
def PrintNTo1(num):
    if num == 0:
        return

    print(num)

    PrintNTo1(num - 1)


if __name__ == "__main__":
    num = 10

    PrintNTo1(num)
