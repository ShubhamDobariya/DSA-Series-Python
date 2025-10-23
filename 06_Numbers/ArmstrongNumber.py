# TC = O(log 10 N)
# SC = O(1)


def ArmstrongNumber(n):
    num = n
    lod = len(str(num))
    total = 0

    while num > 0:
        last_digit = num % 10
        total = total + last_digit**lod
        num = num // 10

    if total == n:
        print(f"{n} is Armstrong Number.")
    else:
        print(f"{n} is not Armstrong Number.")


if __name__ == "__main__":
    n = 153
    ArmstrongNumber(n)
