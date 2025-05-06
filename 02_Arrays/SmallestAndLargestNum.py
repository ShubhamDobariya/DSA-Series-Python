def smallestAndLargetNum(nums):  # TC = O(n), SC = o(1)
    smallest = float("inf")
    largest = float("-inf")

    for num in nums:
        smallest = min(num, smallest)
        largest = max(num, largest)

    return smallest, largest


if __name__ == "__main__":

    nums = [24, 36, 56, 12, 10, 43]

    smalest, largest = smallestAndLargetNum(nums)

    print(f"smallest number is ", smalest)
    print(f"largest number is ", largest)
